import pandas as pd
import matplotlib.pyplot as plt

# Dados fictícios de torcedores do Corinthians em São Paulo, incluindo faixa etária
dados = {
    'ano': [2015, 2016, 2017, 2018, 2019, 2020],
    'numero_torcedores': [22000000, 23000000, 24000000, 23000000, 22000000, 21000000],
    'faixa_etaria_18_30': [7000000, 7500000, 8000000, 7800000, 7500000, 7200000],
    'faixa_etaria_31_50': [8000000, 8500000, 8700000, 8600000, 8300000, 8000000],
    'faixa_etaria_51_mais': [7000000, 7500000, 8000000, 7600000, 6200000, 5800000]
}

# Criar um DataFrame com os dados
df = pd.DataFrame(dados)

# Imprimir os dados
print("Dados dos torcedores do Corinthians em São Paulo:")
print(df)

# Estatísticas básicas
print("\nEstatísticas básicas:")
print(df.describe())

# Visualização dos dados
plt.figure(figsize=(12, 8))

# Gráfico de linha para o número total de torcedores
plt.subplot(2, 1, 1)
plt.plot(df['ano'], df['numero_torcedores'], marker='o', linestyle='-', label='Total de Torcedores')
plt.title('Número de Torcedores do Corinthians em São Paulo (2015-2020)')
plt.xlabel('Ano')
plt.ylabel('Número de Torcedores')
plt.grid(True)
plt.legend()

# Gráfico de barras para a distribuição por faixa etária
plt.subplot(2, 1, 2)
plt.bar(df['ano'], df['faixa_etaria_18_30'], width=0.3, label='18-30 anos')
plt.bar(df['ano'] + 0.3, df['faixa_etaria_31_50'], width=0.3, label='31-50 anos')
plt.bar(df['ano'] + 0.6, df['faixa_etaria_51_mais'], width=0.3, label='51+ anos')
plt.title('Distribuição de Faixa Etária dos Torcedores do Corinthians em São Paulo (2015-2020)')
plt.xlabel('Ano')
plt.ylabel('Número de Torcedores')
plt.xticks(df['ano'] + 0.3, df['ano'])
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()