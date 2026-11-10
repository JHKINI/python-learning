def sales(price, qty):
    return price * qty

p = int(input("가격: "))
q = int(input("수량: "))
print("총액:", sales(p, q))