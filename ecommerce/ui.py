# ===================== ui.py =====================
# The main GUI layout and event handling for the app

import tkinter as tk
from tkinter import messagebox, ttk
from inventory import Inventory
from cart import Cart
from util import format_price, format_product
from receipt import save_receipt

inv = Inventory()
cart = Cart()

def launch_ui():
    root = tk.Tk()
    root.title("AZ Shop")
    root.geometry("900x600")

    frame_top = tk.Frame(root)
    frame_top.pack(side=tk.TOP, fill=tk.X)

    label_title = tk.Label(frame_top, text="E-Commerce Catalog", font=("Helvetica", 18))
    label_title.pack(pady=10)

    search_var = tk.StringVar()
    search_entry = tk.Entry(frame_top, textvariable=search_var, width=30)
    search_entry.pack(side=tk.LEFT, padx=10)
    search_entry.insert(0, "Search products...")

    category_var = tk.StringVar()
    category_dropdown = ttk.Combobox(frame_top, textvariable=category_var, state="readonly")
    categories = ["All"] + sorted(list(set(p.category for p in inv.get_all_products())))
    category_dropdown['values'] = categories
    category_dropdown.current(0)
    category_dropdown.pack(side=tk.LEFT)

    product_frame = tk.Frame(root)
    product_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(product_frame)
    scroll_y = tk.Scrollbar(product_frame, orient="vertical", command=canvas.yview)
    product_container = tk.Frame(canvas)

    product_container.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=product_container, anchor='nw')
    canvas.configure(yscrollcommand=scroll_y.set)

    canvas.pack(side="left", fill="both", expand=True)
    scroll_y.pack(side="right", fill="y")

    cart_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
    cart_frame.pack(side=tk.RIGHT, fill=tk.Y)

    lbl_cart = tk.Label(cart_frame, text="Your Cart", font=("Helvetica", 14))
    lbl_cart.pack(pady=10)

    cart_listbox = tk.Listbox(cart_frame, width=40)
    cart_listbox.pack(pady=5)

    lbl_total = tk.Label(cart_frame, text="Total: ₹0.00", font=("Helvetica", 12))
    lbl_total.pack(pady=5)

    def refresh_cart():
        cart_listbox.delete(0, tk.END)
        total = 0
        for prod, qty in cart.get_cart_items():
            cart_listbox.insert(tk.END, f"{prod.name} x{qty} - {format_price(prod.price * qty)}")
            total += prod.price * qty
        lbl_total.config(text=f"Total: {format_price(total)}")

    def checkout():
        if not cart.items:
            messagebox.showinfo("Cart Empty", "Please add items to the cart first.")
            return
        for pid in cart.items:
            prod, qty = cart.items[pid]
            inv.adjust_stock(pid, qty)
        total = cart.get_total()
        file = save_receipt(cart, total)
        cart.clear_cart()
        refresh_cart()
        messagebox.showinfo("Checkout", f"Order placed! Receipt saved at:\n{file}")

    btn_checkout = tk.Button(cart_frame, text="Checkout", command=checkout)
    btn_checkout.pack(pady=10)

    def show_products(filtered):
        for widget in product_container.winfo_children():
            widget.destroy()
        for prod in filtered:
            frame = tk.Frame(product_container, bd=1, relief=tk.RAISED, padx=5, pady=5)
            frame.pack(fill=tk.X, pady=5, padx=5)
            lbl = tk.Label(frame, text=format_product(prod), anchor='w', justify='left')
            lbl.pack(side=tk.LEFT)

            def add_closure(p=prod):
                def act():
                    cart.add_to_cart(p)
                    refresh_cart()
                return act

            btn = tk.Button(frame, text="Add to Cart", command=add_closure(prod))
            btn.pack(side=tk.RIGHT)

    def filter_products(*args):
        term = search_var.get().lower().strip()
        cat = category_var.get()
        result = inv.get_all_products()
        if cat != "All":
            result = [p for p in result if p.category == cat]
        if term:
            result = [p for p in result if term in p.name.lower() or term in p.desc.lower()]
        show_products(result)

    search_var.trace_add("write", filter_products)
    category_var.trace_add("write", filter_products)

    show_products(inv.get_all_products())
    root.mainloop()