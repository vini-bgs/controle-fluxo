# Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

valor_total = {}
for d in vendas:
    valor_total[d["categoria"]] = valor_total.get([d["categoria"], 0]) + d["valor"] 

print(valor_total)