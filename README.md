# 🛍️ shopping-app-python — A Tkinter-Based E-Commerce Desktop App

**shopping-app-python** is a functional e-commerce desktop application built using Python and Tkinter. It simulates a simplified online store experience — with a real cart, category filtering, and a checkout system that even generates a receipt image!

> 🎯 Built as a college-level project to demonstrate practical Python skills with GUI and file handling.

---

## ✨ Features

- ✅ Clean, scrollable **GUI** using Tkinter
- 🔍 **Live product search** with category filtering (e.g., typing "wireless" shows relevant items)
- 🛒 **Cart system**: add/remove items, update quantities
- 💸 **Checkout**: inventory stock updates and totals calculated
- 🧾 **Receipt generated as an image** (PNG) and saved locally
- 📦 Inventory managed via `inventory.json` — easy to expand or edit

---

## 📁 Folder Structure

shopping-app-python/
├── main.py # Entry point
├── ui.py # All GUI logic
├── cart.py # Shopping cart logic
├── product.py # Product model + JSON loader/saver
├── inventory.py # Inventory class and filtering logic
├── utils.py # Helpers like format_price
├── receipt.py # Creates image receipt
├── data/
│ └── inventory.json # Contains 100+ sample products
├── receipts/
│ └── *.png # Receipts generated on checkout

## 💻 Tech Stack

- **Python 3**
- **Tkinter** — for GUI
- **Pillow (PIL)** — for image-based receipt generation
- **JSON** — for dynamic product data

---

## 📚 Sample Categories in inventory.json

- Clothing

- Electronics

- Accessories

- Stationery

- Home Decor

## 🧠 What I Learned

- Building modular GUI apps with tkinter

- Managing local inventory with json

- Handling cart logic and transactions

- Generating receipts as images (via PIL.ImageDraw)

- Keeping code understandable while adding real features
