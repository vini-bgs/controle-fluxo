# Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

for user in usuarios:
    for id, dado in user.items():
        if dado == "":
            print(f"O usuário {user["nome"]} está com o dado {id} não preenchido. \n"
                  "Favor verificar.")