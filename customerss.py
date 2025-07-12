import tkinter as tk
from tkinter import messagebox
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="customer_db",   # Replace with your actual DB name
    user="postgres",          # Replace if your username is different
    password="Roshni@23"      # Replace actual password
)

cur = conn.cursor()

# ---------------- Save Customer Function ----------------
def save_customer():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()

    if name and email and phone and address:
        try:
            cur.execute(
                "INSERT INTO customers (name, email, phone, address) VALUES (%s, %s, %s, %s)",
                (name, email, phone, address)
            )
            conn.commit()
            messagebox.showinfo("Success", "Customer saved successfully!")

            # Clear form
            name_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            address_entry.delete(0, tk.END)

        except Exception as e:
            conn.rollback()
            messagebox.showerror("Database Error", str(e))
    else:
        messagebox.showwarning("Missing Info", "Please fill in all fields.")

# ---------------- View Customers Function ----------------
def view_customers():
    try:
        view_win = tk.Toplevel(root)
        view_win.title("All Customers")
        view_win.geometry("600x300")

        text_area = tk.Text(view_win, wrap=tk.NONE)
        text_area.pack(fill=tk.BOTH, expand=True)

        scrollbar_y = tk.Scrollbar(view_win, orient=tk.VERTICAL, command=text_area.yview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        text_area.configure(yscrollcommand=scrollbar_y.set)

        scrollbar_x = tk.Scrollbar(view_win, orient=tk.HORIZONTAL, command=text_area.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        text_area.configure(xscrollcommand=scrollbar_x.set)

        # Fetch data
        cur.execute("SELECT name, email, phone, address FROM customers")
        rows = cur.fetchall()

        # Header
        text_area.insert(tk.END, f"{'Name':20} {'Email':30} {'Phone':15} {'Address'}\n")
        text_area.insert(tk.END, "-" * 100 + "\n")

        for row in rows:
            name, email, phone, address = row
            text_area.insert(tk.END, f"{name:20} {email:30} {phone:15} {address}\n")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("Customer Entry App")
root.geometry("400x400")

tk.Label(root, text="Name").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email").pack(pady=5)
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Phone").pack(pady=5)
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Address").pack(pady=5)
address_entry = tk.Entry(root)
address_entry.pack()

tk.Button(root, text="Save Customer", command=save_customer).pack(pady=10)
tk.Button(root, text="View Customers", command=view_customers).pack(pady=5)

root.mainloop()

# ---------------- Close DB Connection After App Closes ----------------
cur.close()
conn.close()