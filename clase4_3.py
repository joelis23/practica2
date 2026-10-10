#Calcular el salario de un empleado , considerando 
#que el salario del empleado consta de un salario 
#base de 200$, 30% de comision y 5% de deducciones 
#del salario basa por concepto de seguro social 

# ENTRADAS : monto_ventas, horas_extras
# salidas : salario_final, comision_ventas,
#            comision_horas ,deducciones 

salario_base = 200 
porc_com_ventas = 30
porc_sso = 5
# entradas
monto_ventas = float(input("Escriba el monto vendido:"))
horas_extras = int(input("Escriba el numero de horas:"))

# proceso 
comision_ventas = monto_ventas*porc_com_ventas/100
comision_horas_extras= horas_extras*5 
deduccion_sso = salario_base * porc_sso /100
bonos = comision_horas_extras + comision_ventas
salario_final = salario_base + bonos - deduccion_sso

# salidas
print(f"La comision por venta es de {comision_ventas:.2f}$")
print(f"La comision por horas extras es de {comision_horas_extras:.2f}$")
print(f"La deduccion por SSO es de {deduccion_sso:.2f}$")
print(f"El salario total es de {salario_final:.2f}$")