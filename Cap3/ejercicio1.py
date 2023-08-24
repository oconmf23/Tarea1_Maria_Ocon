#Ejercicio 1: Reescribe el programa del cálculo del salario para darle al empleado
#1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.

horas = float(input("Introduzca horas: "))
tarifa = float(input("Introduzca tarifa: "))

if horas>40:
    horas_extra = horas - 40
    salario_base = 40 * tarifa
    salario_extra = horas_extra * (tarifa * 1.50)
    salario = salario_base + salario_extra
    print(f'salario: {salario_base + salario_extra}')
else :
    print(f'salario: {horas*tarifa}')
