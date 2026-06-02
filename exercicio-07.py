#  Normalizar uma lista de números para que fiquem na escala de 0 a 1.

try:

    notas = input("Digite as notas dos alunas separando por vírgula: ")

    lista_notas = [int(n.strip()) for n in notas.split(",")]

    minimo = min(lista_notas)
    maximo = max(lista_notas)

    if minimo == maximo:
        raise ValueError("Digite pelo menos dois valores diferentes.")
    
    normalizado = [(x - minimo) / (maximo - minimo) for x in lista_notas]
    print(normalizado)
    
except ValueError as err:
    print(f"Atenção! {err}")