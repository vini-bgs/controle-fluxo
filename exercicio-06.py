# Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = input("Digite um texto: ")

novo_texto = ""
for l in texto:
    if l.isalpha() or l == " ":
        novo_texto += l

lista_palavras = novo_texto.lower().split()

tabela = {}
for p in lista_palavras:
    if p in tabela:
        tabela[p] += 1
    else:
        tabela[p] = 1

print(tabela)