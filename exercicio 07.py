import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


dados = {
    "Produto": ["Notebook", "Celular", "Tablet", "Fone", "Monitor"],
    "Custo": [2500, 1800, 1200, 200, 900],
    "Receita": [3200, 2300, 1700, 350, 1200]
}

df = pd.DataFrame(dados)


df_long = pd.melt(df, id_vars="Produto", value_vars=["Custo", "Receita"],
                  var_name="Tipo", value_name="Valor")


sns.set_theme(style="whitegrid")


plt.figure(figsize=(8, 5))
sns.barplot(
    data=df_long,
    x="Produto", y="Valor",
    hue="Tipo", palette="ch:rot=-.25,hue=1,light=.75",
    alpha=.8, errorbar=None
)


plt.title("Custo e Receita por Produto", fontsize=14, weight="bold")
plt.xlabel("Produto", )
plt.ylabel("Valor (R$)", )
plt.legend(title="")
plt.tight_layout()
plt.show()
