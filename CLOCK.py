import tkinter as tk
from tkinter import Label
import time

# Create the main window
root = tk.Tk()
root.title("Clock and Date")
root.geometry("200x100")
root.attributes('-topmost', True)  # Keep window always on top

# Define function to update time and date
def update_clock():
    current_time = time.strftime('%H:%M:%S')  # Get the current time
    current_date = time.strftime('%d/%m/%Y')   # Get the current date
    label_time.config(text=current_time)       # Update time label
    label_date.config(text=current_date)       # Update date label
    root.after(1000, update_clock)             # Refresh every second

# Create and place labels for time and date
label_time = Label(root, font=('Helvetica', 24), fg='black')
label_time.pack(pady=10)
label_date = Label(root, font=('Helvetica', 18), fg='black')
label_date.pack()

# Start the clock
update_clock()

# Start the main event loop
root.mainloop()
