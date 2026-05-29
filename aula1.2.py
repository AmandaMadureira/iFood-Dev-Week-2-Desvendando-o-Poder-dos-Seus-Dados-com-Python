import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from aula1_1 import nps

NPS_ZONAS =  ["Crítico", "Aperfeiçoamento", "Qualidade", "Excelência"]
NPS_VALORES =  [-100, 0, 50, 75, 100]
NPS_CORES =  ["#FF595E", "#FFCA3A", "#8AC926", "#1982C4"]

def criar_grafico_nps(nps):
    fig, ax = plt.subplots(figsize=(18, 4))

    for i, zona in enumerate(NPS_ZONAS):
        ax.barh([0], width=NPS_VALORES[i+1] - NPS_VALORES[i], left=NPS_VALORES[i], color=NPS_CORES[i])
    ax.barh([0], width=0.5, left=nps, color="black")
    ax.set_yticks([])
    ax.set_xlim(-100, 100)
    ax.set_xticks(NPS_VALORES)

    plt.text(nps, 0, f"{nps:.2f}", ha="center", va="center", color="white", bbox=dict(facecolor="black"))

    patches = [mpatches.Patch(color=NPS_CORES[i], label=NPS_ZONAS[i]) for i in range(len(NPS_ZONAS))]
    plt.legend(handles=patches, bbox_to_anchor=(0,1))

    plt.title("Gráfico de NPS da iFood Dev Week #2")

    plt.show()

criar_grafico_nps(nps)
