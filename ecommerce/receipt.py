# receipt.py
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

def save_receipt(cart, total, folder='receipts'):
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"receipt_{timestamp}.png"
    filepath = os.path.join(folder, filename)

    width, height = 500, 100 + len(cart.items) * 30
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", size=16)
    except:
        font = ImageFont.load_default()

    y = 20
    draw.text((20, y), "E-Commerce Receipt", font=font, fill="black")
    y += 30

    for prod, qty in cart.get_cart_items():
        line = f"{prod.name} x{qty} - ₹{prod.price * qty:.2f}"
        draw.text((20, y), line, font=font, fill="black")
        y += 25

    y += 10
    draw.text((20, y), f"Total: ₹{total:.2f}", font=font, fill="black")

    img.save(filepath)
    try:
        img.show()  # This will open the image on most OS
    except:
        pass

    return filepath
