"""
Dada una Matriz de Identidad nxn
mostrar en color azul solo la diagonal de 1
"""

from colorama import Fore, Style, init
init(autoreset=True)

n = int(input("Ingrese dimensiones de la matriz: "))
matriz = []

# Creamos la matriz identidad
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else: 
            fila.append(0)
    matriz.append(fila)

#Imprimimos mostrando la diagonal en zaul
for i in range(n): 
    for j in range(n):
        if i == j:
            print(Fore.BLUE + str(matriz[i][j]) + Style.RESET_ALL, end=" ")
        else:
            print(matriz[i][j], end=" ")
    print()
n = int(input("Ingrese el tamaño de la matriz (n): "))

print(f"\nMatriz de Identidad {n}x{n} con diagonal azul:\n")

# Codigos ANSI para colerear en la terminal

AZUL = "\033[24m"
RESET = "\033[0m"

# Genear y recorrer la matriz
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:

#Si etamos en la diagonal principal, ponemos un 1 en azul

          fila.append(f"{AZUL}1{RESET}")
        else:

# Si no, ponemos un 0 normal 
            fila.append("0")

# Imprimir la fila uniendo los elementos con un espacio 

print(" ".join(fila))