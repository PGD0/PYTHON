
"""
    1. La compañía «ALAS» incrementa el valor de sus pasajes en un 30% en alta 
    temporada mientras que la compañía «VOLAR» lo incrementa en solo 20%.
    2. Ambas compañías descuentan el 50% si el pasajero es menor de edad; además la 
    compañía «VOLAR» tiene un recargo de $100000 para los mayores de 60 años para 
    cubrir el seguro de vida.
    3. Los estudiantes que viajan por «ALAS» y que no son menores de edad, tienen un 
    descuento del 10% en temporada baja.
    4. La tarifa básica Bogotá-Tokio reglamentaria es de 5 millones de pesos.
    """


def calcular_precio_pasaje(pasajero: dict) -> int:
    costoReglamentario = 5000000
    totalPagar = costoReglamentario

    if (pasajero['compania'] == 'ALAS'):
        if (pasajero['temporada'] == 'ALTA'):
            totalPagar += (costoReglamentario*0.3)
        if pasajero['edad'] < 18:
            totalPagar -= (costoReglamentario*0.5)
        if (pasajero['edad'] > 18) and (pasajero['estudiante'] == True):
            totalPagar -= costoReglamentario*0.1

    elif (pasajero['compania'] == 'VOLAR'):
        if (pasajero['temporada'] == 'ALTA'):
            totalPagar += (costoReglamentario*0.2)
        if pasajero['edad'] < 18:
            totalPagar -= (costoReglamentario*0.5)
        elif pasajero['edad'] > 60:
            totalPagar += 100000
    print(totalPagar)


calcular_precio_pasaje(pasajero={
    'temporada': 'BAJA',
    'compania': 'VOLAR',
    'edad': 70,
    'estudiante': False
})
