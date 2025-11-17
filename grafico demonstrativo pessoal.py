import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


dados = {
    "Habilidades": ["Inglês basico", "Pacote Office", "Conhecimento em Python", "Trabalho em equipe", "Proatividade", "Flexibilidade e adaptação"],
    "Nivel": [50, 60, 40, 80, 95, 95]
}

df = pd.DataFrame(dados)

sns.barplot(x="Habilidades", y="Nivel", data=df, palette="rocket_r")

plt.title("Gráfico Demonstrativo")
plt.xlabel("Habilidades")
plt.ylabel("Nível (%)")

plt.subplots_adjust(bottom=0.30)

plt.tight_layout()
plt.show()
