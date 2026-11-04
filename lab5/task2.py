a = int(input())
b = int(input())
c = 0
n = 1
if b >= a:
    for x in range(a, b + 1):
        c += x
        n *= x
    print(f"Сумма: {c}")
    print(f"Произведение: {n}")
#2
#5