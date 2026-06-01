# Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. Escreva um programa que valide essas condições e imprima Dados de usuário válidos ou o erro específico encontrado.

try:
    
    idade = input("Qual a sua idade? ")
    idade = int(idade)

    if idade < 18 or idade > 65:
        print("Não é possível criar uma conta.")
        exit()

    email = input("Qual o seu e-mail? ")   

    if "@gmail.com" not in email:
        print("E-mail inválido.")
        exit()

    print("Dados válidos!")    

except ValueError:
    print("Error")
