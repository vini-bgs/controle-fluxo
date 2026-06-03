# Processar itens de uma lista até encontrar um valor específico que indica a parada.


num_secreto = 3

while True:
    try:
        num_escolhido = int(input("Tenten acertar o número de 0 a 10 que estou pensando :p "))

        if num_escolhido == num_secreto:
            print("Parabéns, você acertou!")
            break

        print("Que pena, você errou. Tente novamente!")

    except ValueError as err:
        print(f"Atenção! {err}.")


