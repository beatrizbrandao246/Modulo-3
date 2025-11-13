import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


dados = {
    "Região": ["Sul", "Sudeste", "Centro-Oeste", "Nordeste", "Norte"],
    "Vendas": [35000, 52000, 27000, 31000, 18000]
}

df = pd.DataFrame(dados)

sns.barplot(x="Região", y="Vendas", data=df, palette= "rocket_r")

plt.title("Vendas por Região")
plt.show()