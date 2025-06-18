import json

class Product:
    def __init__(self, pid, name, price, category, stock, desc):
        self.pid = pid
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock
        self.desc = desc

    def to_dict(self):
        return {
            "pid": self.pid,
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "stock": self.stock,
            "desc": self.desc
        }

def load_products(filepath='data/inventory.json'):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            print(f"Loaded {len(data)} products from inventory.")
            return [Product(**prod) for prod in data]
    except Exception as e:
        print("Error loading inventory:", e)
        return []


def save_products(products, filepath='data/inventory.json'):
    try:
        with open(filepath, 'w') as f:
            json.dump([p.to_dict() for p in products], f, indent=4)
    except Exception as e:
        print("Error saving inventory:", e)
