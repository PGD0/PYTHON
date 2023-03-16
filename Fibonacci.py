

def recur_fibo(n: int):
    # Creamos al secuencia Fibonacci
    fibonacci = []
    n1 = 0
    n2 = 1
    n3 = 0
    for i in range(n):
        fibonacci.append(n1)
        n3 = n2 + n1
        n1 = n2
        n2 = n3
    return fibonacci


def iniciar_aplicacion(n: int):
    fibonacci = []
    n1 = 0
    n2 = 1
    n3 = 0
    for i in range(n):
        fibonacci.append(n1)
        n3 = n2 + n1
        n1 = n2
        n2 = n3
    # Usamos un array para subir valor por valor a su exponente al cubo de la secuencia Fibonacci
    fibonacciElv = []
    for i in range(len(fibonacci)):
        fibonacciElv.append(fibonacci[i]**3)
    print(fibonacciElv)


iniciar_aplicacion(10)
