count = 0
sum = 0
while True:
    data = input()
    if data == "stop":
        break
    count += 1
    sum += int(data)
if count == 0:
    print("Нет покупок")
else:
    print(f"Покупок: {count}")
    print(f"Общая стоимость: {sum}")
    print(f"Средня стоимость: {(sum / count):.2f}")