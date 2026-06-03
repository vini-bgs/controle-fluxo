# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

lista_dados = []
dado = ""

while True:

    dado = input("Entre com o dado desejado: ")

    if dado.lower().strip() == "sair":
        print("Encerrando...")
        break

    lista_dados.append(dado)

print(lista_dados) 