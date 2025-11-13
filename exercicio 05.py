import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dados = {
    "Aplicativo": ["Instagram", "TikTok", "WhatsApp", "YouTube", "X (Twitter)"],
    "Minutos por dia": [95, 110, 80, 120, 60]
}

df = pd.DataFrame(dados)

sns.barplot(x="Aplicativo", y="Minutos por dia", data=df, palette= "crest")

plt.title("Vendas por Região")
plt.show()