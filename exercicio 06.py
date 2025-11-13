import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


dados = {
    "Setor": ["Financeiro", "Comercial", "TI", "RH", "Marketing",
              "Comercial", "TI", "Financeiro", "Marketing", "RH"],
    "Idade": [34, 29, 25, 41, 28, 33, 26, 38, 31, 45]
}

df = pd.DataFrame(dados)


sns.set_theme(style="whitegrid")


g = sns.catplot(
    data=df,
    kind="bar",
    x="Setor",
    y="Idade",
    errorbar="sd",   
    palette="dark",     
    alpha=.6,           
    height=6             
)


g.despine(left=True)
g.set_axis_labels("", "Idade Média")
g.fig.suptitle("Média de Idade por Setor",)
 

plt.tight_layout()
plt.show()
