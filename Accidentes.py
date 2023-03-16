import pandas as pd

data = pd.read_csv('Accidentalidad_en_Barranquilla.csv', header=0)
print(data)

calle30 = data[data.SITIO_EXACTO_ACCIDENTE == 'CL 30 CR 8']


def accidente(data: pd.DataFrame) -> dict:
    # Conseguimos la cantidad total de Accidente de Gravedad
    valores = calle30['GRAVEDAD_ACCIDENTE'].value_counts().to_list()
    suma = 0
    for i in range(len(valores)):
        suma += valores[i]
    print(
        f"La cantidad total de accidentes de gravedad en la calle 30 son de: {suma}")
    # Conseguimos el accidente que mas se repite y la cantidad de veces que lo hace
    accidenteMO = calle30['CLASE_ACCIDENTE'].value_counts().keys().tolist()
    val1 = accidenteMO[0]
    numAccidenteOC = calle30['CLASE_ACCIDENTE'].value_counts().tolist()
    val2 = numAccidenteOC[0]
    print(
        f"El tipo de accidente que mas se repite en la calle 30 es: {accidenteMO[0]}")
    # Conseguimos la mayor cantidad de heridos en un accidente con su respectiva fecha
    valores3 = calle30['CANT_HERIDOS_EN _SITIO_ACCIDENTE'].max()
    part = calle30[['FECHA_ACCIDENTE', 'CANT_HERIDOS_EN _SITIO_ACCIDENTE']]
    ejem1 = part.sort_values(
        by='CANT_HERIDOS_EN _SITIO_ACCIDENTE', ascending=False)
    ejem2 = ejem1.iloc[0, :]
    valoresSeparados = ejem2.tolist()
    fecha = valoresSeparados[0]
    cantHeridos = valoresSeparados[1]
    print(
        f"La cantidad maxima de heridos en un accidente de la calle 30 es de: {valores3}")
    # Creamos el diccionario con los valores obtenidos anteriormente
    diccionarioFinal = {
        'clase_mas_accidente': (val1, val2),
        'accidentes_gravedad': suma,
        'cantidad_max_heridos': (cantHeridos, fecha)
    }
    # Imprimimos
    print(diccionarioFinal)


accidente(data)
