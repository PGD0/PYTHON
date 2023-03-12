import pandas as pd


data1 = {
    'ESTRATO': {
        'F': 8284,
        'M': 9321
    }
}
print(pd.DataFrame(data1))

data2 = {
    'PUNT_GLOBAL': {
        'HUILA': 251.92,
        'CASANARE': 252.43,
        'META': 253.17,
        'NARINO': 254.87,
        'QUINDIO': 254.98,
        'RISARALDA': 255.77,
        'CUNDINAMARCA': 257.64,
        'BOYACA': 262.90,
        'SANTANDER': 265.85,
        'BOGOTA': 267.88
    }
}
print(pd.DataFrame(data2))

resultado = {**data1, **data2}
print(resultado)
