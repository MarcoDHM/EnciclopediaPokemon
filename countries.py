# Definición de la lista 'countries' que contiene nombres de países
countries = ["France", "Uruguay", "Germany", "Netherlands", "Ghana"]

# Imprime el segundo país en la lista 'countries'
print("Second country:", countries[1])

# Imprime el quinto país en la lista 'countries'
print("Fifth country:", countries[4])

# Definición de la lista 'countries_capitals' con nombres de países y sus capitales
countries_capitals = [
    ["France", "Uruguay", "Germany", "Ghana"],
    ["Paris", "Montevideo", "Berlin", "Accra"]
]

# Accede al primer país en la primera sub-lista y lo almacena en la variable 'first_country'
first_country = countries_capitals[0][0]

# Se asegura de que el primer país sea "France" mediante una afirmación (assert)
assert first_country == "France"

# Imprime el primer país almacenado en la variable 'first_country'
print("First country:", first_country)

# Accede a la lista de capitales (segunda sub-lista)
capitals = countries_capitals[1]

# Accede a la primera capital en la lista de capitales y la imprime
first_capital = capitals[0]
print(f"The first capital is {first_capital}.")

# Modificaciones en la lista 'countries'
countries.remove("Germany")  # Elimina "Germany" de la lista 'countries'
print("Countries after removing 'Germany':", countries)

del countries[2]  # Elimina el tercer elemento de la lista 'countries'
assert "Germany" not in countries  # Se asegura de que "Germany" no esté en la lista
print("Countries after deleting element at index 2:", countries)

countries.sort()  # Ordena la lista 'countries' de forma ascendente
print("Sorted countries:", countries)

countries.sort(reverse=True)  # Ordena la lista 'countries' de forma descendente
print("Reverse sorted countries:", countries)
