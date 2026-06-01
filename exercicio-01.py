# Você está analisando um conjunto de dados de vendas e 
# 
# precisa garantir que todos os registros tenham valores positivos para quantidade e preço. 
# 
# Escreva um programa que verifique esses campos e imprima Dados válidos se ambos forem positivos ou Dados inválidos caso contrário.

try:

    quantidade = input("Informe a quantidade: ")
    preco = input("Informe o preço: ")

    quantidade = int(quantidade)
    preco = float(quantidade)
    total = quantidade * preco

    if quantidade < 0 or preco < 0:
        print("Dados inválidos")

    else:
        print(f"Dados válidos. Como a quantidade é {quantidade} e preço R${preco} o total fica igual a R${total}.")

except ValueError as err:
    print(f"{err}")