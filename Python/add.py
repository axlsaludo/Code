import tkinter as tk
import serial
import time

# Establish connection to Arduino
ser = serial.Serial('COM3', 9600, timeout=1)  # Change 'COM3' to your correct COM port
time.sleep(2)  # Allow some time for the connection to establish

# Function to send command to Arduino
def move_stepper(direction):
    if direction == "UP":
        ser.write(b'UP\n')
    elif direction == "DOWN":
        ser.write(b'DOWN\n')
    
    # Read the response from Arduino (if any)
    response = ser.readline().decode().strip()
    if response:
        status_label.config(text=response)

# Create the tkinter window
root = tk.Tk()
root.title("Stepper Motor Control")

# Create the UP button
up_button = tk.Button(root, text="Move Up", command=lambda: move_stepper("UP"), width=20, height=2)
up_button.pack(pady=10)

# Create the DOWN button
down_button = tk.Button(root, text="Move Down", command=lambda: move_stepper("DOWN"), width=20, height=2)
down_button.pack(pady=10)

# Create a label to display the status
status_label = tk.Label(root, text="Status", font=("Arial", 14))
status_label.pack(pady=20)

# Start the tkinter main loop
root.mainloop()

# Close the serial connection on exit
ser.close()
