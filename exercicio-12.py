# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

while True:

    num = input("Digite um número entre 1 e 10: ")

    try:
        num = int(num)

        if num in range(1,11):
            print(f"Certo. O número escolhido foi {num}")
            break
        else:
            raise ValueError("Você não digitou um número de 1 até 10.")
        
    except ValueError as err:
        print(f"Atenção! {err}.")