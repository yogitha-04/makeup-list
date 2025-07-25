import tkinter as tk

root = tk.Tk()

root.geometry("2000x900")
root.title("Makeup Products List")
root.config(bg='light green')

title_label = tk.Label(root, text="Listing the Makeup Products", font=("Algerian", 25, "bold"), bg='light green')
title_label.place(x=400, y=50)

product_label = tk.Label(root, text="Available Products:", font=("Arial", 16, "bold"), bg='light green')
product_label.place(x=200, y=150)

products = [
    "Foundation",
    "Concealer",
    "Lipstick",
    "Eyeliner",
    "Mascara",
    "Blush",
    "Highlighter",
    "Eyeshadow Palette",
    "Makeup Remover",
    "Primer",
    "Setting Spray",
    "Bronzer"
]

product_listbox = tk.Listbox(root, font=("Arial", 14), width=40, height=15)
for product in products:
    product_listbox.insert(tk.END, product)
product_listbox.place(x=200, y=200)

close_button = tk.Button(root, text="CLOSE", font=("Arial", 12), command=root.destroy)
close_button.place(x=700, y=600)

root.mainloop()
