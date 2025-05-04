import tkinter as tk
from tkinter import messagebox

def show_message():
    """Displays a message box."""
    messagebox.showinfo("Message", "Hello, Windows User!")

# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Create the button
button = tk.Button(root, text="Click Me", command=show_message)
button.pack(pady=20) # Add some padding

# Start the Tkinter event loop
root.mainloop()
