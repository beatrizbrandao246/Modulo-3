import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


dados = {
    "Cliente": ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Gabriela", "Heitor"],
    "Satisfação": [8.5, 6.0, 9.0, 7.5, 8.0, 5.5, 9.5, 7.0],
    "Categoria": ["Premium", "Básico", "Premium", "Básico", "Premium", "Básico", "Premium", "Básico"]
}

df = pd.DataFrame(dados)


sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))


sns.violinplot(
    data=df,
    x="Categoria", y="Satisfação",
    bw_adjust=.5, cut=1, linewidth=1.2,
    palette="Set3", inner="box"
)


plt.title("Feedback dos Clientes", fontsize=14, weight="bold")
plt.xlabel("Categoria", fontsize=12)
plt.ylabel("Nível de Satisfação", fontsize=12)
plt.ylim(0, 10)
sns.despine(left=True, bottom=True)


plt.tight_layout()
plt.show()
