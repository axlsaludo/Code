import tkinter as tk
from tkinter import messagebox
import serial
import threading
import time

# Configure the serial connection
SERIAL_PORT = 'COM3'  # Replace with your Arduino's COM port
BAUD_RATE = 9600

class ArduinoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Arduino Control Interface")
        
        # Initial states
        self.garage_state = tk.StringVar(value="Unknown")
        self.auto_light_control_state = tk.StringVar(value="Unknown")
        self.ir_sensor_state = tk.StringVar(value="Unknown")
        self.led_states = [tk.StringVar(value="Off") for _ in range(5)]
        
        # Initialize Serial Connection
        try:
            self.serial_connection = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        except serial.SerialException:
            messagebox.showerror("Connection Error", f"Unable to open port {SERIAL_PORT}")
            self.root.quit()
            return
        
        # UI Components
        self.create_ui()
        
        # Reset states after UI components are created
        self.reset_all_states()

        # Start thread to read serial data
        self.read_thread = threading.Thread(target=self.read_serial_data, daemon=True)
        self.read_thread.start()

    def create_ui(self):
        # Command buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        commands = [
            ("Open Garage Door", "garage door open"),
            ("Close Garage Door", "garage door close"),
            ("Lock Garage", "lock garage"),
            ("Unlock Garage", "unlock garage"),
            ("Toggle Auto Light Control", "toggle auto light control"),
            ("Disable IR Sensor", "disable IR sensor"),
            ("Enable IR Sensor", "enable IR sensor"),
            ("Reset LEDs", "reset LEDs")
        ]

        for (text, command) in commands:
            button = tk.Button(button_frame, text=text, command=lambda cmd=command: self.send_command(cmd))
            button.pack(side=tk.LEFT, padx=5)

        # LED Control and State Display
        self.led_control_frame = tk.Frame(self.root)
        self.led_control_frame.pack(pady=10)
        
        self.led_label = tk.Label(self.led_control_frame, text="Set LED (format: X:Y, -1:0 to reset all)")
        self.led_label.pack(side=tk.LEFT)
        
        self.led_entry = tk.Entry(self.led_control_frame)
        self.led_entry.pack(side=tk.LEFT, padx=5)
        
        self.led_button = tk.Button(self.led_control_frame, text="Send", command=self.send_led_command)
        self.led_button.pack(side=tk.LEFT)

        # Status display for garage door and other components
        self.status_frame = tk.Frame(self.root)
        self.status_frame.pack(pady=10)
        
        tk.Label(self.status_frame, text="Garage Door: ").grid(row=0, column=0, sticky="e")
        tk.Label(self.status_frame, textvariable=self.garage_state).grid(row=0, column=1, sticky="w")
        
        tk.Label(self.status_frame, text="Auto Light Control: ").grid(row=1, column=0, sticky="e")
        tk.Label(self.status_frame, textvariable=self.auto_light_control_state).grid(row=1, column=1, sticky="w")
        
        tk.Label(self.status_frame, text="IR Sensor: ").grid(row=2, column=0, sticky="e")
        tk.Label(self.status_frame, textvariable=self.ir_sensor_state).grid(row=2, column=1, sticky="w")
        
        for i in range(5):
            tk.Label(self.status_frame, text=f"LED {i}: ").grid(row=3+i, column=0, sticky="e")
            tk.Label(self.status_frame, textvariable=self.led_states[i]).grid(row=3+i, column=1, sticky="w")

        # Text widget for displaying feedback
        self.feedback_display = tk.Text(self.root, height=10, width=50)
        self.feedback_display.pack(pady=10)

    def send_command(self, command):
        if self.serial_connection.is_open:
            self.serial_connection.write(f"{command}\n".encode())
            self.display_feedback(f"Sent: {command}")
            if command == "reset LEDs":
                self.reset_all_led_states()
        else:
            self.display_feedback("Error: Serial connection not open")

    def send_led_command(self):
        led_command = self.led_entry.get()
        if led_command:
            self.send_command(led_command)
            self.led_entry.delete(0, tk.END)

    def display_feedback(self, message):
        self.feedback_display.insert(tk.END, message + "\n")
        self.feedback_display.see(tk.END)

    def read_serial_data(self):
        while True:
            if self.serial_connection.is_open and self.serial_connection.in_waiting > 0:
                data = self.serial_connection.readline().decode('utf-8').strip()
                if data:
                    self.display_feedback(f"Received: {data}")
                    self.update_states(data)

    def update_states(self, data):
        if "Garage door opening" in data or "Garage door closing" in data:
            self.garage_state.set("Open" if "opening" in data else "Closed")
        elif "Garage door locked" in data:
            self.garage_state.set("Locked")
        elif "Garage door unlocked" in data:
            self.garage_state.set("Unlocked")
        elif "Automatic light control enabled" in data:
            self.auto_light_control_state.set("Enabled")
        elif "Automatic light control disabled" in data:
            self.auto_light_control_state.set("Disabled")
        elif "IR sensor enabled" in data:
            self.ir_sensor_state.set("Enabled")
        elif "IR sensor disabled" in data:
            self.ir_sensor_state.set("Disabled")
        elif "LED " in data:
            parts = data.split(" ")
            led_num = int(parts[1])
            state = parts[-1] == "on."
            self.led_states[led_num].set("On" if state else "Off")
        elif "All LEDs turned off" in data:
            self.reset_all_led_states()

    def reset_all_led_states(self):
        for state in self.led_states:
            state.set("Off")

    def reset_all_states(self):
        # Send initial reset commands
        self.send_command("reset LEDs")
        self.send_command("unlock garage")
        self.send_command("disable IR sensor")
        self.send_command("toggle auto light control")
        
        # Reset state variables
        self.garage_state.set("Unlocked")
        self.auto_light_control_state.set("Disabled")
        self.ir_sensor_state.set("Disabled")
        self.reset_all_led_states()

    def close(self):
        if self.serial_connection.is_open:
            self.serial_connection.close()
        self.root.destroy()

# Create the main window
root = tk.Tk()
app = ArduinoGUI(root)

# Graceful exit
root.protocol("WM_DELETE_WINDOW", app.close)
root.mainloop()
