def ingresar_motocicletas():
    motocicletas = []
    for i in range(3):
        moto = input("Ingrese una marca de motocicleta: ")
        motocicletas.append(moto)
    return motocicletas

def mostrar_motocicletas(motocicletas):
    print("Estas son las motocicletas que ingresaste:")
    for moto in motocicletas:
        print(moto)

def seleccionar_motocicleta(motocicletas):
    seleccion = input("Ingrese número de la motocicleta que desea (1, 2 o 3): ")
    while seleccion not in ["1", "2", "3"]:
        seleccion = input("Selección inválida. Por favor, ingrese (1, 2 o 3): ")
    seleccion = int(seleccion)
    print("La motocicleta seleccionada es:", motocicletas[seleccion-1])

# Pedir al usuario que ingrese las motocicletas
motocicletas = ingresar_motocicletas()

# Mostrar las motocicletas ingresadas
mostrar_motocicletas(motocicletas)

# Llamar a la función para seleccionar una motocicleta
seleccionar_motocicleta(motocicletas)
