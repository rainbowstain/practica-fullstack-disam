monto = 10000
if monto > 12000:
    print("El monto es mayor a 12000")
elif monto == 12000:
    print("El monto es igual a 12000")
else:
    print("El monto es menor a 12000")  

print(f"El monto es {monto}", "y", "es menor a 12000" if monto < 12000 else "es mayor o igual a 12000")