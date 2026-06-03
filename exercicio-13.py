# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

while True:
    try:
        n_paginas = int(input("Qual a quantidade de páginas a ser consumida? "))

        break

    except ValueError as err:
        print(f"Atenção! {err}")

pagina_atual = 1

while pagina_atual < n_paginas:
    print(f"Processando página {pagina_atual}/{n_paginas}...")
    pagina_atual += 1

print(f"Processamento completo! ({pagina_atual}/{n_paginas})")