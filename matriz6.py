from colorama import Fore, Style, init
init(autoreset=True)

# Función para mostrar matrices con formato ordenado
def mostrar_matriz(matriz, titulo="Matriz"):
    if not matriz:
        print(f"\n{Fore.RED}[{titulo}] está vacía. Crea una primero.")
        return
    print(f"\n{Fore.YELLOW}--- {titulo} ---")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            # Si es una matriz cuadrada y es la diagonal principal, la pinta de azul
            if len(matriz) == len(matriz[i]) and i == j:
                print(Fore.BLUE + str(matriz[i][j]), end=" ")
            else:
                print(Fore.WHITE + str(matriz[i][j]), end=" ")
        print()

# Función para rellenar matrices dinámicas (nxn)
def pedir_matriz(nombre, tamano):
    matriz = []
    print(f"\n{Fore.MAGENTA}--- Ingresar valores para {nombre} ({tamano}x{tamano}) ---")
    for i in range(tamano):
        fila = []
        for j in range(tamano):
            while True:
                try:
                    valor = int(input(f"Posición [{i}][{j}]: "))
                    fila.append(valor)
                    break
                except ValueError:
                    print(f"{Fore.RED}Por favor, ingresa un número entero válido.")
        matriz.append(fila)
    return matriz

# Función para sumar matrices
def sumar_matrices(m1, m2):
    if not m1 or not m2:
        print(f"\n{Fore.RED}Error: Ambas matrices deben estar creadas.")
        return None
    tamano = len(m1)
    return [[m1[i][j] + m2[i][j] for j in range(tamano)] for i in range(tamano)]

# Función para multiplicar matrices (Fila x Columna)
def multiplicar_matrices(m1, m2):
    if not m1 or not m2:
        print(f"\n{Fore.RED}Error: Ambas matrices deben estar creadas.")
        return None
    tamano = len(m1)
    resultado = [[0 for _ in range(tamano)] for _ in range(tamano)]
    for i in range(tamano):
        for j in range(tamano):
            for k in range(tamano):
                resultado[i][j] += m1[i][k] * m2[k][j]
    return resultado

# Función para generar la matriz identidad dinámica que hiciste
def crear_identidad(tamano):
    matriz = []
    for i in range(tamano):
        fila = []
        for j in range(tamano):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz

# Menú principal interactivo a color
def menu():
    matriz_A = []
    matriz_B = []
    tamano = 3 # Tamaño por defecto, se puede cambiar en la opción 1
    
    while True:
        print(f"\n{Fore.GREEN}{Style.BRIGHT}==================== MENÚ DE MATRICES EXPERTO ====================")
        print("1. Definir tamaño e ingresar Matriz A y B")
        print("2. Mostrar Matrices Actuales")
        print("3. Sumar Matriz A + Matriz B")
        print("4. Multiplicar Matriz A x Matriz B")
        print("5. Generar Matriz Identidad Personalizada (Diagonal Azul)")
        print(f"{Fore.RED}6. Salir")
        
        opcion = input(f"\n{Fore.YELLOW}Elige una opción (1-6): ")
        
        if opcion == '1':
            tamano = int(input(f"{Fore.CYAN}¿De qué tamaño deseas las matrices (ej. 3 para 3x3)?: "))
            matriz_A = pedir_matriz("Matriz A", tamano)
            matriz_B = pedir_matriz("Matriz B", tamano)
            print(f"\n{Fore.GREEN}¡Matrices creadas con éxito!")
            
        elif opcion == '2':
            mostrar_matriz(matriz_A, "Matriz A")
            mostrar_matriz(matriz_B, "Matriz B")
            
        elif opcion == '3':
            resultado_suma = sumar_matrices(matriz_A, matriz_B)
            if resultado_suma:
                mostrar_matriz(resultado_suma, "Resultado de la Suma (A + B)")
                
        elif opcion == '4':
            resultado_mult = multiplicar_matrices(matriz_A, matriz_B)
            if resultado_mult:
                mostrar_matriz(resultado_mult, "Resultado de la Multiplicación (A x B)")
                
        elif opcion == '5':
            n = int(input(f"{Fore.CYAN}Ingrese dimensiones para la Matriz Identidad: "))
            m_identidad = crear_identidad(n)
            mostrar_matriz(m_identidad, f"Matriz Identidad {n}x{n}")
            
        elif opcion == '6':
            print(f"\n{Fore.LIGHTRED_EX}Saliendo del programa. ¡Buen trabajo!")
            break
        else:
            print(f"\n{Fore.RED}Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    menu()