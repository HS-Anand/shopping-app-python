def format_price(price):
    return f"₹{price:.2f}"

def format_product(product):
    return f"{product.name} ({product.category})\n{format_price(product.price)} | Stock: {product.stock}\n{product.desc}"

def apply_discount(total, percent):
    if percent <= 0 or percent > 100:
        return total
    return total - (total * percent / 100)