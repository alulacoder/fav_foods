from tkinter import *

# Create a root window.
top = Tk()
top.title("My Favorite Dishes")

# Create listbox object with modified colors and foods
listbox = Listbox(top, height=10,
                  width=20,
                  bg="lightblue",  # Change background color
                  activestyle='dotbox',
                  font="Helvetica",
                  fg="darkgreen")  # Change text color

# Define the size of the window.
top.geometry("300x250")

# Define a label for the list.
label = Label(top, text=" FOOD ITEMS")

# Insert new elements by their index and names.
listbox.insert(1, "Sushi")
listbox.insert(2, "Tacos")
listbox.insert(3, "Pasta")
listbox.insert(4, "Salad")
listbox.insert(5, "Steak")

# Pack the widgets
label.pack()
listbox.pack()

# Display until the user exits themselves.
top.mainloop()
