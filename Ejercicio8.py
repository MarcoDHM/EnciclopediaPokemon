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

# Pedir al usuario que ingrese las motocicletas
motocicletas = ingresar_motocicletas()

# Mostrar las motocicletas ingresadas
mostrar_motocicletas(motocicletas)
