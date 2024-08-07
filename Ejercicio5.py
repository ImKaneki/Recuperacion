def sumar_numeros(*numeros):
    suma = sum(numeros)
    return suma

def multiplicar_numeros(*numeros):
    producto = 1
    for num in numeros:
        producto *= num
    return producto

# Ejemplo de uso
resultado_suma = sumar_numeros(1, 2, 3, 4)
print(f"La suma de los números es: {resultado_suma}")

resultado_multip = multiplicar_numeros(1, 2, 3, 4, 5)
print(f"El producto de los números es: {resultado_multip}")