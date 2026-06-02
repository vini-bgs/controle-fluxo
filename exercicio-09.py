# Dada uma lista de números, extrair apenas aqueles que são pares.

try:

    numeros = input("Digite uma lista de números inteiros separados por vírgula: ")

    lista_numeros = [int(n) for n in numeros.split(",")]

    lista_pares = []
    for n in lista_numeros:
        if n % 2 == 0:
            lista_pares.append(n)

    print(f"Da lista informada esses são os números pares: {lista_pares}.")

except ValueError:
    print("ValueError")