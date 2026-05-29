import pandas as pd

dados = pd.read_csv("dados.csv", delimiter=";")

def calcular_nps(notas):
    detratores = sum(notas.apply(lambda nota: nota <= 6))
    promotores = notas[notas >= 9].count()

    return (promotores - detratores) / len(notas) * 100

nps = calcular_nps(dados['nota'])

print(nps)