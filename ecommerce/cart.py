from product import Product

class Cart:
    def __init__(self):
        self.items = {}  # pid: [product, qty]

    def add_to_cart(self, product, qty=1):
        if product.pid in self.items:
            self.items[product.pid][1] += qty
        else:
            self.items[product.pid] = [product, qty]

    def remove_from_cart(self, pid):
        if pid in self.items:
            del self.items[pid]

    def update_quantity(self, pid, qty):
        if pid in self.items:
            if qty <= 0:
                del self.items[pid]
            else:
                self.items[pid][1] = qty

    def clear_cart(self):
        self.items.clear()

    def get_total(self):
        return sum(prod.price * qty for prod, qty in self.items.values())

    def get_cart_items(self):
        return self.items.values()

    def to_dict(self):
        return {pid: {"qty": qty, **prod.to_dict()} for pid, (prod, qty) in self.items.items()}

    def from_dict(self, cart_dict):
        self.items = {}
        for pid, data in cart_dict.items():
            prod = Product(
                pid=data["pid"],
                name=data["name"],
                price=data["price"],
                category=data["category"],
                stock=data["stock"],
                desc=data["desc"]
            )
            self.items[pid] = [prod, data["qty"]]
