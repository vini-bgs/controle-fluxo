# Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
#
#Temperatura < 18°C é 'Baixa'
#Temperatura >= 18°C e <= 26°C é 'Normal'
#Temperatura > 26°C é 'Alta'

try:

    temperatura = input("Qual a temperatura? ")

    temperatura = float(temperatura)

    if temperatura < 18:
        leitura = "Baixa"

    elif 18 <= temperatura <= 26:
        leitura = "Normal"

    else:
        leitura = "Alta"

    print(f"De acordo com a temperatura informada a leitura está {leitura}.")

except ValueError:
    print("Erro")