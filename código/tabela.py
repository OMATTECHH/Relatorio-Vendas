import matplotlib.pyplot as plt
import pandas as pd

# Pergunta o nome da pessoa que quer ver os dados
usuario = input("Olá! Qual é o seu nome? ")

# Lista de funcionários (Nome, Idade, Vendas)
funcionarios = [
    ("Carlos", 25, 120),
    ("Mariana", 30, 150),
    ("João", 22, 90),
    ("Fernanda", 35, 180),
    ("Ricardo", 28, 130),
]

# Criando um DataFrame
df = pd.DataFrame(funcionarios, columns=["Nome", "Idade", "Vendas"])

# Ordenando os funcionários pelo número de vendas
df_ordenado = df.sort_values(by="Vendas", ascending=False)

# Melhor, pior e meio
melhor = df_ordenado.iloc[0]
pior = df_ordenado.iloc[-1]
meio = df_ordenado.iloc[len(df_ordenado) // 2]

# Exibindo os resultados
print("\n--- RELATÓRIO DE VENDAS ---")
print(df.to_string(index=False))
print(f"\nMelhor funcionário: {melhor['Nome']} com {melhor['Vendas']} vendas.")
print(f"Pior funcionário: {pior['Nome']} com {pior['Vendas']} vendas.")
print(f"Funcionário do meio: {meio['Nome']} com {meio['Vendas']} vendas.")

# Perguntar se o usuário quer ver um gráfico
resposta = input("\nVocê quer ver um gráfico visual das vendas? (s/n): ").strip().lower()

if resposta == 's':
    plt.figure(figsize=(8, 5))
    plt.bar(df["Nome"], df["Vendas"], color="skyblue", edgecolor="black")
    plt.xlabel("Funcionários")
    plt.ylabel("Vendas")
    plt.title("Vendas por Funcionário")
    plt.xticks(rotation=25)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Exibir valores nas barras
    for i, v in enumerate(df["Vendas"]):
        plt.text(i, v + 5, str(v), ha="center", fontsize=10, fontweight="bold")

    plt.show()

# Agradecendo ao usuário
print(f"\nObrigado por usar nosso sistema, {usuario}! Tenha um ótimo dia! 😊")