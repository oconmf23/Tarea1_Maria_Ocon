#Ejercicio 2: Reescribe el programa del salario usando try y except, de modo que el
#programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando
#un mensaje y saliendo del programa.

try:
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
except:
    print("Error, por favor introduzca un número")