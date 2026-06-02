#  Normalizar uma lista de números para que fiquem na escala de 0 a 1.

try:
    
    notas = input("Digite as notas dos alunas separando por vírgula: ")

    lista_notas = []

    for n in notas.split(","):
        lista_notas.append(int(n))

    minimo = min(lista_notas)
    maximo = max(lista_notas)

    normalizado = [

        (x - minimo) / (maximo - minimo) for x in lista_notas

    ]

    print(normalizado)

except ValueError:
    print("Erro")