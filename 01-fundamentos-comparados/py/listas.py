montos = [100, 200, 300, 400, 500]
montos.append(600)
print(str(montos) + " estos son los montos")

for monto in montos:
    print(monto)

for i in range(10):
    print(i)

for i in range(len(montos)):
    print((1 + i), "-", montos[i])

montos2 = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
for lista in montos2:
    print(lista)

mayores = []

for monto in montos2:
    if monto > 10000:
        mayores.append(monto)
print(f"Montos originales: {montos2}")
print(f"Montos mayores a 10000: {mayores}") 
print(f"Cantidad: {len(mayores)}")
for mayore in mayores:
    if mayore > 50000:
        print(f"{mayore} - director")
    elif mayore > 10000:
        print(f"{mayore} - jefe")
