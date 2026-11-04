n = int(input())
count = 0
for x in range(n):
    val = 1
    for y in range(x + 1):
        if val % 2 != 0:
            count += 1
        print(val, end=" ")
        val = val * (x - y) // (y + 1)
    print()
print(f"Нечетных элементов: {count}")