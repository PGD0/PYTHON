import pandas as pd
from operator import itemgetter

data = pd.read_csv('data.csv', header=0)
print(data)


def distribucionGeneroEstrato(data: pd.DataFrame, estrato: int):
    n = 0
    estrato = 0
    while (n == 0):
        numEstrato = int(input("Digite un estrato del 1 al 6: "))
        estrato = f"Estrato {numEstrato}"
        if numEstrato < 1 or numEstrato > 6:
            print("El estrato ingresado no existe")
        else:
            n = 1
        hombres = (data.iloc[:, 2][data.ESTRATO == estrato]
                   [data.GENERO == "M"].value_counts())[0]
        mujeres = (data.iloc[:, 2][data.ESTRATO == estrato]
                   [data.GENERO == "F"].value_counts())[0]

    df = pd.DataFrame({'ESTRATO': {'F': mujeres, 'M': hombres}})
    print(df)
    df1 = df.to_dict()
    return df1


def diezMejores(data: pd.DataFrame):
    departamentos = list((data.iloc[:, 1].unique()))
    departamentos.sort()
    mejores = {}
    for i in departamentos:
        promedio = data.iloc[:, -1][data.DEPARTAMENTO == i].mean()
        mejores[i] = promedio
    mejores = dict(sorted(mejores.items(), key=itemgetter(1), reverse=True))
    n = 0
    while (n == 0):
        if (len(mejores.items()) == 10):
            n = 1
        else:
            mejores.popitem()
    departamentos = list(mejores.keys())
    departamentos.reverse()
    puntajes = list(mejores.values())
    puntajes.reverse()
    df2 = dict()
    for i in range(len(departamentos)):
        df2[departamentos[i]] = puntajes[i]
    Comb = zip(departamentos, puntajes)
    list1 = list(Comb)
    df2_1 = pd.DataFrame(list1, columns=['DEPARTAMENTOS', 'PUNT_GLOBAL'])
    print(df2_1)
    return df2


combinacion1 = distribucionGeneroEstrato(data, int)
combinacion2 = diezMejores(data)


def combinarAmbasDataframes(data: pd.DataFrame, estrato: int):
    total = combinacion1 | combinacion2
    print(total)


combinarAmbasDataframes(data, int)
