montos = [100, 200, 300, 400, 500]
montos.append(600)
print(str(montos) + " estos son los montos")

for monto in montos:
    print(monto)

for i in range(10):
    print(i)

for i in range(len(montos)):
    print((1 + i), "-", montos[i])