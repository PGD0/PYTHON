
"""
    Implemente una función que sea capaz de descifrar mensajes codificados con el cifrado de 
    César, teniendo en cuenta que el corrimiento usado puede ser cualquiera (no necesariamente 
    3). La función recibirá el valor del corrimiento como parámetro. Use el alfabeto ASCII para 
    su solución que es predeterminado en Python.
    """


def descifrar_codigo_cesar(texto_cifrado: str, corrimiento: int) -> str:
    # Texto cifrado
    minusculas = []
    mayusculas = []
    for i in range(65, 91):
        mayusculas.append(chr(i))
    for i in range(97, 123):
        minusculas.append(chr(i))

    palabra = ""
    for i in range(len(texto_cifrado)):
        if texto_cifrado[i].isupper():
            for j1 in range(len(mayusculas)):
                if texto_cifrado[i] == mayusculas[j1]:
                    cont = j1-corrimiento
                    palabra += mayusculas[cont]
        elif texto_cifrado[i].islower():
            for j2 in range(len(minusculas)):
                if texto_cifrado[i] == minusculas[j2]:
                    cont2 = j2-corrimiento
                    palabra += minusculas[cont2]
        else:
            palabra += texto_cifrado[i]
    return palabra


# Casos publicos
print(descifrar_codigo_cesar("Lspe", 4))
print(descifrar_codigo_cesar("Tvmqivs tmirws, pyiks ibmwxs", 4))
print(descifrar_codigo_cesar("Ho ghvfliudgr fhvdu hv idflo", 3))
print("--------------------------------")
# Casos ocultos
print(descifrar_codigo_cesar("CNQJC", 2))
print(descifrar_codigo_cesar("Wfaovu pz lhzf", 7))
print(descifrar_codigo_cesar("Alclnpelxzw", 11))
