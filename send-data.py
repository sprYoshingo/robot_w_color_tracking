import serial
import time
import tkinter as tk
from tkinter import messagebox

#setup serial
try:
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1) #my arduino com port change as needed
    time.sleep(2)  #reset time
except serial.SerialException:
    arduino = None
    print("failed to connect to arduino.")

#GUI setup
def send_command(cmd):
    if arduino and arduino.is_open:
        arduino.write(cmd.encode())
    else:
        messagebox.showerror("Error", "Arduino not connected")

#create window
root = tk.Tk()
root.title("im not seeing enought movement")
root.geometry("500x500")
root.configure(bg="#000000")

button_style = {"width": 12, "height": 2, "font": ("Arial", 12, "bold")}
label_style = {"fg": "white", "bg": "#000000", "font": ("Papyrus", 16, "bold")}

#button functions
def forward():
    send_command("F")

def backward():
    send_command("B")

def stop():
    send_command("S")

def right_forward():
    send_command("R")

def left_forward():
    send_command("L")

def right_backwards(): #moves the right/left wheels backwards; which means it goes the opposite direction
    send_command("X")

def left_backwards():
    send_command("Q")

#layout
tk.Label(root, text="Rodger Rodger", **label_style).pack(pady=10)

frame = tk.Frame(root, bg="#000000")
frame.pack()


tk.Button(frame, text="Left\nBackward", command=left_backwards, **button_style).grid(row=2, column=0, padx=5, pady=5)
tk.Button(frame, text="Backward", command=backward, **button_style).grid(row=2, column=1, padx=5, pady=5)
tk.Button(frame, text="Right\nBackward", command=right_backwards, **button_style).grid(row=2, column=2, padx=5, pady=5)

tk.Button(frame, text="Left\nForward", command=left_forward, **button_style).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="Stop", command=stop, bg="#ff0000", fg="white", **button_style).grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame, text="Right\nForward", command=right_forward, **button_style).grid(row=0, column=2, padx=5, pady=5)

tk.Button(frame, text="Forward", command=forward, **button_style).grid(row=0, column=1, padx=5, pady=10)

#close serial on exit
def on_close():
    if arduino:
        arduino.close()
    root.destroy()

def on_key_press(event): #kill the program on key press
    print(f"Key '{event.keysym}' pressed. Exiting program.")
    on_close()

root.protocol("WM_DELETE_WINDOW", on_close)
root.bind("<Key>", on_key_press)
root.mainloop()
