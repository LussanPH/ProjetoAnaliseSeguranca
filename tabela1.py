import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

tabela = pd.read_excel("ProjetoSegurancaCeara\PLANILHA Anuário Brasileiro de Segurança Pública 2024.xlsx", sheet_name="Copia T43")

#print(tabela)

x = tabela.columns[1:7].tolist()

y = tabela.iloc[5, 1:7].tolist()

print(x)
print(y)

fig, ax = plt.subplots()
barras = ax.bar(x, y, width=0.5)
ax.bar_label(barras)
plt.title("Número de casos com armas de fogo no Ceará")
plt.xlabel("Anos")
plt.ylabel("Valores")
plt.show()
