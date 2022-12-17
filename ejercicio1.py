"""
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""

name = input("Ingrese el nombre: ")
numero = int(input("Ingrese el número: "))

print((name + "\n") * numero)
