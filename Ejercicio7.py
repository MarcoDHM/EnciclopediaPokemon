motorcycles = ['honda', 'yamaha', 'suzuki']

# Mostrar la lista original
print("Lista original de motocicletas:", motorcycles)

# Solicitar al usuario la nueva marca
posicion = int(input("Introduce la posición (0, 1 o 2) que deseas cambiar: "))
nueva_marca = input("Introduce la nueva marca: ")

# Verificar si la posición es válida
if 0 <= posicion < len(motorcycles):
    # Cambiar la marca en la posición indicada por el usuario
    motorcycles[posicion] = nueva_marca
    print("Lista actualizada de motocicletas:", motorcycles)
else:
    print("Posición no válida. Debes introducir 0, 1 o 2.")
