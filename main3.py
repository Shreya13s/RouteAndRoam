import tkinter as tk
from tkinter import ttk, messagebox
from module4 import PlacesModule

# ---------------- BACKEND ----------------
mod = PlacesModule("places.csv")

# ---------------- FUNCTIONS ----------------
def next_clicked():
    country = country_var.get().strip()

    if not country:
        messagebox.showwarning("Input Error", "Please select a country")
        return

    places = mod.list_places_by_country(country)

    output_list.delete(0, tk.END)

    if not places:
        output_list.insert(tk.END, "No places found")
    else:
        for place in places:
            output_list.insert(tk.END, place.title())

# ---------------- UI ----------------
root = tk.Tk()
root.title("Route & Roam – Vacation Planner")
root.geometry("520x420")
root.resizable(False, False)

# Title
tk.Label(
    root,
    text="Route & Roam – Vacation Planner",
    font=("Helvetica", 18, "bold")
).pack(pady=20)

# Country label
tk.Label(
    root,
    text="Select a Country",
    font=("Helvetica", 12)
).pack(pady=5)

# Dropdown
country_var = tk.StringVar()
country_dropdown = ttk.Combobox(
    root,
    textvariable=country_var,
    state="readonly",
    width=30
)

# 🔹 Add countries present in your CSV
country_dropdown["values"] = [
    "Thailand",
    "India",
    "Italy",
    "France",
    "Maldives"
]

country_dropdown.current(0)
country_dropdown.pack(pady=10)

# Next button
tk.Button(
    root,
    text="Next",
    width=20,
    bg="#c47a2c",
    fg="white",
    font=("Helvetica", 11, "bold"),
    command=next_clicked
).pack(pady=15)

# Output list
output_list = tk.Listbox(root, width=55, height=8)
output_list.pack(pady=10)

# Run app
root.mainloop()

    
