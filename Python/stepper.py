import serial
import tkinter as tk

# Set up the serial connection (adjust COM port as needed)
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's port

def move_up():
    ser.write(b'U')  # Send 'U' to start moving up

def move_down():
    ser.write(b'D')  # Send 'D' to start moving down

def stop_moving():
    ser.write(b'S')  # Send 'S' to stop the motor

# Create the main window
root = tk.Tk()
root.title("Stepper Motor Control")

# Create buttons and attach them to the functions
up_button = tk.Button(root, text="Move Up", command=move_up)
down_button = tk.Button(root, text="Move Down", command=move_down)
stop_button = tk.Button(root, text="Stop", command=stop_moving)

# Place the buttons in the window
up_button.pack(pady=10)
down_button.pack(pady=10)
stop_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
