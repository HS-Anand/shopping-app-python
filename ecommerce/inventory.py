from product import load_products, save_products

class Inventory:
    def __init__(self):
        self.products = load_products()

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, pid):
        for prod in self.products:
            if prod.pid == pid:
                return prod
        return None

    def adjust_stock(self, pid, qty):
        for prod in self.products:
            if prod.pid == pid:
                prod.stock -= qty
                break
        save_products(self.products)

    def restore_stock(self, pid, qty):
        for prod in self.products:
            if prod.pid == pid:
                prod.stock += qty
                break
        save_products(self.products)

    def filter_by_category(self, category):
        return [p for p in self.products if p.category == category]

    def search_by_name(self, term):
        return [p for p in self.products if term.lower() in p.name.lower()]
