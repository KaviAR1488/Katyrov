def print_receipt(date,*items,discount=0):
    total=0
    print(f"Дата:{date}")
    print("Товары:")
    for name,price,quantity in items:
        cost=price*quantity
        total+=cost
        print(f"{name}:{price}руб×{quantity}={cost}руб")
    if discount>0:
        discount_amount=total*discount/100
        total-=discount_amount
        print(f"Скидка{discount}%:-{discount_amount:.2f}руб")
    print(f"Итого:{total:.2f}руб")