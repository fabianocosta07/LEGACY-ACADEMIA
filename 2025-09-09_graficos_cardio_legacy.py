import matplotlib.pyplot as plt
import numpy as np

# Paleta Legacy
azul_neon = "#233dff"
azul_escuro = "#050a30"
off_white = "#f4f6fc"

# ---------- Gráfico 1: Cárdio x Pizza ----------
plt.figure(figsize=(6,4))
atividades = ["30 min corrida", "60 min corrida", "90 min corrida", "Pizza média"]
calorias = [300, 600, 900, 1500]

bars = plt.bar(atividades, calorias, color=[azul_neon, azul_neon, azul_neon, "red"])
plt.ylabel("Calorias (kcal)", color=off_white)
plt.title("Cárdio x Pizza (impacto calórico)", color=off_white, fontsize=12)
plt.xticks(rotation=20, color=off_white)
plt.yticks(color=off_white)
plt.gca().set_facecolor(azul_escuro)
plt.gcf().patch.set_facecolor(azul_escuro)

# ---------- Gráfico 2: Estratégias ----------
plt.figure(figsize=(6,4))
estrategias = ["Cárdio sozinho", "Dieta ajustada", "Mix Legacy"]
resultados = [1, 3, 5]  # escala fictícia de eficácia

plt.bar(estrategias, resultados, color=["gray", azul_neon, "green"])
plt.ylabel("Efetividade no emagrecimento", color=off_white)
plt.title("Estratégias de Emagrecimento", color=off_white, fontsize=12)
plt.xticks(rotation=15, color=off_white)
plt.yticks(color=off_white)
plt.gca().set_facecolor(azul_escuro)
plt.gcf().patch.set_facecolor(azul_escuro)

# ---------- Gráfico 3: Passos x Calorias ----------
plt.figure(figsize=(6,4))
passos = [3000, 7000, 10000]
calorias_gastas = [120, 280, 400]

plt.plot(passos, calorias_gastas, marker='o', color=azul_neon, linewidth=2)
plt.fill_between(passos, calorias_gastas, color=azul_neon, alpha=0.3)
plt.xlabel("Passos por dia", color=off_white)
plt.ylabel("Calorias (kcal)", color=off_white)
plt.title("Impacto dos Passos Diários", color=off_white, fontsize=12)
plt.xticks(color=off_white)
plt.yticks(color=off_white)
plt.gca().set_facecolor(azul_escuro)
plt.gcf().patch.set_facecolor(azul_escuro)

plt.show()
