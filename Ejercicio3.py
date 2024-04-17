def comprueba(lista, nombre_enviado):
  if nombre_enviado in lista and nombre_enviado.startswith("A"):
    return ("Sí, permiso activo")
  else:
    return ("No, permiso denegado")

usuarios = ["Ana", "Beto", "Carlos", "Alicia", "David", "Elena", "Alberto", "Fernanda", "Gonzalo", "Andrea"]

print("Lista de usuarios")
for elemento in usuarios:
  print(elemento, end=" ")
print() # para imprimir una línea en blanco
nombre_ingresado = input("Ingrese un nombre de usuario: ")
resultado = comprueba(usuarios, nombre_ingresado)
print (resultado)
