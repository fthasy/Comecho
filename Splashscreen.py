# Faith Simi_As

# Import module
from tkinter import *

# Create the splash root object
splash_root = Tk()

# Adjust size
splash_root.geometry("300x400")

# Load the image
image = PhotoImage(file="Splashscreen.png")

# Set Label for the image
splash_image_label = Label(splash_root, image=image)
splash_image_label.pack()

# Set Label for text
splash_label = Label(splash_root, text="splash screen", font=18)
splash_label.pack()

# Main window function
def main():
    # Destroy splash window
    splash_root.destroy()

    # Execute tkinter
    root = Tk()

    # Adjust size
    root.geometry("300x400")

# set Interval
splash_root.after(3000, main)

# Execute tkinter
mainloop()