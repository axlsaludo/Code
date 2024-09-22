import tkinter as tk
from tkinter import messagebox
import serial
import time

# Arduino COM port and baud rate
arduino_port = 'COM3'  # Update this with your actual COM port
baud_rate = 9600

# Serial communication setup
arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2)  # Allow time for Arduino to reset

def send_command(command):
    """Send command to Arduino and read response."""
    arduino.write((command + '\n').encode())
    time.sleep(1)  # Small delay for Arduino to process
    response = arduino.readline().decode().strip()
    return response

def toggle_led(led_index):
    command = f"toggle led{led_index}"
    response = send_command(command)
    messagebox.showinfo("Response", response)

def read_dht():
    response = send_command("read dht")
    messagebox.showinfo("DHT Sensor Data", response)

def read_ir():
    response = send_command("read ir")
    messagebox.showinfo("IR Sensor Data", response)

def move_motor():
    cycles = motor_cycles.get()
    command = f"move motor {cycles}"
    response = send_command(command)
    messagebox.showinfo("Motor Response", response)

def toggle_fan1():
    response = send_command("toggle fan1")
    messagebox.showinfo("Fan 1 Response", response)

def toggle_fan2():
    response = send_command("toggle fan2")
    messagebox.showinfo("Fan 2 Response", response)

def read_ldr():
    response = send_command("read ldr")
    messagebox.showinfo("LDR Sensor Data", response)

def get_sensor_data():
    """Get all sensor data and display."""
    dht_data = send_command("read dht")
    ir_data = send_command("read ir")
    ldr_data = send_command("read ldr")
    messagebox.showinfo("All Sensor Data", f"{dht_data}\n{ir_data}\n{ldr_data}")

# Create the main application window
root = tk.Tk()
root.title("Arduino Control Panel")

# Create and place widgets
tk.Label(root, text="Control LEDs").grid(row=0, column=0, columnspan=2)
for i in range(5):
    tk.Button(root, text=f"Toggle LED {i}", command=lambda i=i: toggle_led(i)).grid(row=i+1, column=0, padx=5, pady=5)

tk.Label(root, text="Motor Control").grid(row=0, column=2, columnspan=2)
tk.Label(root, text="Motor Cycles:").grid(row=1, column=2, padx=5, pady=5)
motor_cycles = tk.Entry(root)
motor_cycles.grid(row=1, column=3, padx=5, pady=5)
tk.Button(root, text="Move Motor", command=move_motor).grid(row=2, column=2, columnspan=2, padx=5, pady=5)

tk.Label(root, text="Sensor Data").grid(row=5, column=0, columnspan=4)
tk.Button(root, text="Read DHT", command=read_dht).grid(row=6, column=0, padx=5, pady=5)
tk.Button(root, text="Read IR", command=read_ir).grid(row=6, column=1, padx=5, pady=5)
tk.Button(root, text="Read LDR", command=read_ldr).grid(row=6, column=2, padx=5, pady=5)
tk.Button(root, text="Get All Sensor Data", command=get_sensor_data).grid(row=6, column=3, padx=5, pady=5)

tk.Label(root, text="Fan Control").grid(row=7, column=0, columnspan=2)
tk.Button(root, text="Toggle Fan 1", command=toggle_fan1).grid(row=8, column=0, padx=5, pady=5)
tk.Button(root, text="Toggle Fan 2", command=toggle_fan2).grid(row=8, column=1, padx=5, pady=5)

# Run the application
root.mainloop()
