# Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

valor_total = {}
for d in vendas:
    if d["categoria"] not in valor_total:
        valor_total[d["categoria"]] = d["valor"]
    else:
        valor_total[d["categoria"]] += d["valor"]

print(valor_total)