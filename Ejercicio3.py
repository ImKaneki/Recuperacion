def calcular_longitud(lista_o_cadena):
    count = 0
    for _ in lista_o_cadena:
        count += 1
    return count

# Ejemplo de uso con una lista
lista_ejemplo = [1, 2, 3, 4, 5, 6, 7,]
longitud_lista = calcular_longitud(lista_ejemplo)
print(f"La longitud de la lista es: {longitud_lista}")

# Ejemplo de uso con una cadena
cadena_ejemplo = "Hola Tierra"
longitud_cadena = calcular_longitud(cadena_ejemplo)
print(f"La longitud de la cadena es: {longitud_cadena}")