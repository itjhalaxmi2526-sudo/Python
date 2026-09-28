import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Glow & Grace Salon")
root.geometry("480x600")
root.configure(bg="#FCE4EC")

# Heading
tk.Label(root, text="GLOW & GRACE SALON",
         font=("Arial", 20, "bold"),
         bg="#D81B60", fg="white").pack(fill="x", pady=10)

frame = tk.Frame(root, bg="#FCE4EC")
frame.pack(pady=10)

# Customer Name
tk.Label(frame, text="Customer Name", bg="#FCE4EC").grid(row=0, column=0, pady=8)
name = tk.Entry(frame, width=25)
name.grid(row=0, column=1)

# Phone
tk.Label(frame, text="Phone Number", bg="#FCE4EC").grid(row=1, column=0, pady=8)
phone = tk.Entry(frame, width=25)
phone.grid(row=1, column=1)

# Gender
tk.Label(frame, text="Gender", bg="#FCE4EC").grid(row=2, column=0, pady=8)

gender = tk.StringVar(value="Female")
tk.Radiobutton(frame, text="Female", variable=gender,
               value="Female", bg="#FCE4EC").grid(row=2, column=1, sticky="w")
tk.Radiobutton(frame, text="Male", variable=gender,
               value="Male", bg="#FCE4EC").grid(row=2, column=1, padx=90)

# Service
tk.Label(frame, text="Service", bg="#FCE4EC").grid(row=3, column=0, pady=8)

service = tk.StringVar(value="Haircut - ₹300")
services = [
    "Haircut - ₹300",
    "Hair Spa - ₹700",
    "Facial - ₹800",
    "Manicure - ₹500",
    "Pedicure - ₹600"
]

tk.OptionMenu(frame, service, *services).grid(row=3, column=1)

# Date
tk.Label(frame, text="Appointment Date", bg="#FCE4EC").grid(row=4, column=0, pady=8)
date = tk.Entry(frame, width=25)
date.grid(row=4, column=1)

# Time
tk.Label(frame, text="Appointment Time", bg="#FCE4EC").grid(row=5, column=0, pady=8)
time = tk.Entry(frame, width=25)
time.grid(row=5, column=1)

# Payment
tk.Label(frame, text="Payment", bg="#FCE4EC").grid(row=6, column=0, pady=8)

payment = tk.StringVar(value="Cash")
tk.Radiobutton(frame, text="Cash", variable=payment,
               value="Cash", bg="#FCE4EC").grid(row=6, column=1, sticky="w")
tk.Radiobutton(frame, text="UPI", variable=payment,
               value="UPI", bg="#FCE4EC").grid(row=6, column=1, padx=90)


# Booking Function
def book():
    if name.get() == "":
        messagebox.showerror("Error", "Please enter Customer Name")
    elif phone.get() == "":
        messagebox.showerror("Error", "Please enter Phone Number")
    elif date.get() == "":
        messagebox.showerror("Error", "Please enter Appointment Date")
    elif time.get() == "":
        messagebox.showerror("Error", "Please enter Appointment Time")
    else:
        messagebox.showinfo(
            "Booking Confirmed",
            "GLOW & GRACE SALON\n\n"
            "Customer: " + name.get() +
            "\nPhone: " + phone.get() +
            "\nGender: " + gender.get() +
            "\nService: " + service.get() +
            "\nDate: " + date.get() +
            "\nTime: " + time.get() +
            "\nPayment: " + payment.get() +
            "\n\nAppointment Booked Successfully!"
        )


# Buttons
tk.Button(root, text="BOOK APPOINTMENT",
          command=book,
          bg="#D81B60", fg="white",
          font=("Arial", 11, "bold"),
          width=20).pack(pady=15)

tk.Button(root, text="EXIT",
          command=root.destroy,
          bg="#AD1457", fg="white",
          width=10).pack()

root.mainloop()
