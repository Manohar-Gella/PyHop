import tkinter as tk
from tkinter import messagebox


def book_ticket():
    name = name_entry.get()
    age = age_entry.get()
    num_tickets = num_tickets_entry.get()
    show = show_choice.get()

    if name == "" or age == "" or num_tickets == "" or show == "":
        messagebox.showerror("Error", "Please fill in all fields.")
    else:
        confirmation = "Name: {}\nAge: {}\nNumber of Tickets: {}\nShow: {}".format(name, age, num_tickets, show)
        messagebox.showinfo("Confirmation", confirmation)


root = tk.Tk()
root.title("Ticket Booking Portal")

# Labels
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e")
tk.Label(root, text="Age:").grid(row=1, column=0, sticky="e")
tk.Label(root, text="Number of Tickets:").grid(row=2, column=0, sticky="e")
tk.Label(root, text="Select Show:").grid(row=3, column=0, sticky="e")

# Entries
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)
num_tickets_entry = tk.Entry(root)
num_tickets_entry.grid(row=2, column=1)

# Radio Buttons
show_choice = tk.StringVar()
show_choice.set("Matinee")
tk.Radiobutton(root, text="Matinee", variable=show_choice, value="Matinee").grid(row=3, column=1, sticky="w")
tk.Radiobutton(root, text="Evening", variable=show_choice, value="Evening").grid(row=4, column=1, sticky="w")

# Submit Button
tk.Button(root, text="Book Ticket", command=book_ticket).grid(row=5, column=1, pady=10)

root.mainloop()
