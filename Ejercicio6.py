print("Días de la semana")
dato = input("Introduce número del 0 al 6: ")
num = int(dato)

dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

if 0 <= num <= 6:
    print("El día introducido es:", dias[num])
else:
    print("Número no válido. Debes introducir un número del 0 al 6.")
