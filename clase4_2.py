import random

gastos_enero = random.randint (200,1000)
gastos_febrero = random.randint (200,1000)
gastos_marzo = random.randint (200,1000)
numero_meses = 3

total_gastos = gastos_enero + gastos_febrero + gastos_marzo
promedio_gastos = total_gastos / numero_meses 

print (f"El gasto del mes de enero es {gastos_enero}:")
print (f"El gasto del mes de febrero es {gastos_febrero}:")
print (f"El gasto del mes de marzo es{gastos_marzo}:")

print (f"El monto total gastado fue  {total_gastos:.2f}")
