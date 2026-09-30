#Suma de matrices
""" Leer 2 matrices 3 x 3 y sumar en una matriz """
matrizA = []
for i in range(3):
    matrizA.append([])
    for j in range(3):
        valor = int(input((f"Fila {i +1}, columna {j+1}: ")))
        matrizA.append(valor)

for fila in matrizA:
    print(fila)

#Agregar matriz B
matrizB = []
for i in range(3):
    matrizB.append([])
    for j in range (3):
        valor = int(input((f"Fila {i+1}, columna {j+1}: ")))
        matrizB[i].append(valor)

#sumar matrices 
matrizC = []
for i in range(len(matrizA)):