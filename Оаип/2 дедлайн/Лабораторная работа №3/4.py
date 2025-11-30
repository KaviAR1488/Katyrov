products = {"Ноутбук": {"price": 50000, "sold": 15},"Мышь": {"price": 1000, "sold": 45},"Клавиатура": {"price": 2500, "sold": 30},"Монитор": {"price": 30000, "sold": 8}}
max_sold = max(products.items(), key=lambda x: x[1]["sold"])
print(f"Самый продаваемый: {max_sold[0]}")
total_revenue = sum(product["price"] * product["sold"] for product in products.values())
print(f"Общая выручка: {total_revenue}")
max_revenue_product = max(products.items(), key=lambda x: x[1]["price"] * x[1]["sold"])
print(f"Товар с макс выручкой: {max_revenue_product[0]}")