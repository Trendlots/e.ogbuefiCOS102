import tkinter as tk
from tkinter import messagebox


def calculate_price():
    location = location_entry.get().lower()
    try:
        weight = float(weight_entry.get())
    except ValueError:
        messagebox.showerror(
            "Invalid input", "Please enter a valid number for weight")
        return

    if location == "ibeju-lekki":
        if weight >= 10:
            price = 5000
        else:
            price = 3500
    elif location == "epe":
        if weight >= 10:
            price = 10000
        else:
            price = 5000
    else:
        messagebox.showerror("Invalid location",
                             "Please enter 'Ibeju-Lekki' or 'Epe'")
        return

    messagebox.showinfo("Delivery Price", f"The delivery fee is ₦{price}")


# GUI setup
root = tk.Tk()
root.title("Delivery Fee Checker")

tk.Label(root, text="Enter location (Ibeju-Lekki or Epe):").pack()
location_entry = tk.Entry(root)
location_entry.pack()

tk.Label(root, text="Enter package weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Button(root, text="Calculate Price", command=calculate_price).pack()

root.mainloop()
