#Ejercicio 3: Escribe un programa para pedirle al usuario el número de
#horas y la tarifa por hora para calcular el salario bruto.

horas = float(input("Introduzca horas: "))
tarifa = float(input("Introduzca tarifa: "))
salario = horas*tarifa
print(f'salario: {horas*tarifa}')
