info = input()
num, let, rig, time, money = info.split(";")
print(f"Поезд: {num}")
print(f"Маршрут: {let + ' - ' + rig}")
print(f"Отправление: {time}")
print(f"Цена: {float(money):.2f}")
#T-18;Владивосток;Хабаровск;08:45;1850.5