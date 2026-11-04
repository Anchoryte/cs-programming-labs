n = int(input())
n0 = 0
n1 = 0
n2 = 0
for x in range(n):
    c = float(input())
    if c == 0:
        n0 += 1
    elif c > 0:
        n1 += 1
    else:
        n2 += 1
print(f"Ниже нуля: {n2}")
print(f"Равны нулю: {n0}")
print(f"Выше нуля: {n1}")



#5
#-2.5
#0
#3.1
#-1
#0