import serial
import tkinter as tk

# Set up the serial connection (adjust COM port as needed)
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's port

# Define the functions for the buttons
def move_up():
    ser.write(b'U')  # Send 'U' for up

def move_down():
    ser.write(b'D')  # Send 'D' for down

# Create the main window
root = tk.Tk()
root.title("Stepper Motor Control")

# Create buttons and attach them to the functions
up_button = tk.Button(root, text="Move Up", command=move_up)
down_button = tk.Button(root, text="Move Down", command=move_down)

# Place the buttons in the window
up_button.pack(pady=1)
down_button.pack(pady=1)

# Start the Tkinter event loop
root.mainloop()
