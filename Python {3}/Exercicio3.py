import json

# Carregar dados do JSON
with open('faturamento.json') as f:
    dados = json.load(f)

faturamentoDiario = [dia["valor"] for dia in dados["faturamento_diario"] if dia["valor"] > 0]

# Calculando o menor e o maior valor de faturamento
menorFaturamento = min(faturamentoDiario)
maiorFaturamento = max(faturamentoDiario)

# Calculando a média de faturamento
mediaFaturamento = sum(faturamentoDiario) / len(faturamentoDiario)

# Contando os dias com faturamento acima da média
diasAcimaMedia = sum(1 for valor in faturamentoDiario if valor > mediaFaturamento)

# Exibindo os resultados
print(f"Menor valor de faturamento: {menorFaturamento}")
print(f"Maior valor de faturamento: {maiorFaturamento}")
print(f"Número de dias com faturamento acima da média: {diasAcimaMedia}")