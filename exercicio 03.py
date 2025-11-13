import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dados = {
    "Funcionário": ["Alice", "Bruno", "Carlos", "Diana", "Eduardo", "Fernanda", "Gustavo", "Helena"],
    "Produtividade": [82, 74, 90, 65, 77, 88, 93, 70],
    "Horas_Semanais": [40, 36, 42, 30, 38, 44, 45, 35]
}

df = pd.DataFrame(dados)

sns.set_theme(style="whitegrid")
palette = sns.color_palette("rocket_r", as_cmap=False)


sns.barplot(
    x="Funcionário",
    y="Produtividade",
    hue="Horas_Semanais",
    palette=palette,
    data=df
)


plt.title("Nível de Produtividade por Funcionário",)
plt.xlabel("Funcionário")
plt.ylabel("Produtividade")
plt.legend(title="Horas Semanais")
plt.show()
