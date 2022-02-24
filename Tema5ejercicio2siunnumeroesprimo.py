#Escribe una función que pueda decirte si un número (número entero) es primo o no.
def numeroprimo():
    for n in range(2,numeroentero):
        if numeroentero % n == 0:
            print('No es primo', n, 'es divisor')
            return False
    print('Es primo, sólo son divisibles por uno y por sí mismos.\nSe entiende por divisible a que el resultado sea un número entero, es decir, no decimal.')
    return True

numeroentero=int(input('Introduce un número entero:'))
numeroprimo()