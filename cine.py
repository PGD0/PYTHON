def calcular_costo_boletas(info_cine: dict) -> int:
    dinamix = 18800
    _3d = 15500
    _2d = 11300
    total = 0

    if (info_cine['tipo_sala'] == "Dinamix"):
        if (info_cine['hora_pico'] == False):
            dinamix = dinamix - (dinamix*0.1)
        else:
            dinamix = dinamix + (dinamix*0.5)
        if (info_cine['pago_tarjeta_cine'] == True):
            dinamix = dinamix - (dinamix * 0.05)
        if (info_cine['reserva'] == True):
            dinamix = dinamix + 2000

        if (info_cine['cantidad_boletas'] >= 3):
            dinamix = dinamix - 500
            total = (dinamix * info_cine['cantidad_boletas'])
        else:
            total = dinamix * info_cine['cantidad_boletas']
    # return print(total)
    elif (info_cine['tipo_sala'] == "3D"):
        if (info_cine['hora_pico'] == False):
            _3d = _3d - (_3d*0.1)
        else:
            _3d = _3d + (_3d*0.25)
        if (info_cine['pago_tarjeta_cine'] == True):
            _3d = _3d - (_3d * 0.05)
        if (info_cine['reserva'] == True):
            _3d += 2000

        if (info_cine['cantidad_boletas'] >= 3):
            _3d = _3d - 500
            total = (_3d * info_cine['cantidad_boletas'])
        else:
            total = _3d * info_cine['cantidad_boletas']
    elif (info_cine['tipo_sala'] == "2D"):
        if (info_cine['hora_pico'] == False):
            _2d = _2d - (_2d*0.1)
        else:
            _2d = _2d + (_2d*0.25)
        if (info_cine['pago_tarjeta_cine'] == True):
            _2d = _2d - (_2d * 0.05)
        if (info_cine['reserva'] == True):
            _2d += 2000

        if (info_cine['cantidad_boletas'] >= 3):
            _2d = _2d - 500
            total = (_2d * info_cine['cantidad_boletas'])
        else:
            total = _2d * info_cine['cantidad_boletas']
    return print(round(total))


calcular_costo_boletas(info_cine={
    'cantidad_boletas': 3,
    'tipo_sala': '2D',
    'hora_pico': False,
    'pago_tarjeta_cine': False,
    'reserva': True
})
