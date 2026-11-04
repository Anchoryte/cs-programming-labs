a = int(input())
b = int(input())
if a < 0 or b < 0 \
    or a + b == 0:
    print("Ошибка")
nod = (a % b)
print(nod)
