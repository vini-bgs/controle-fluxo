#  Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

n_tentativa = 1

while n_tentativa < 5:
    print(f"Conectando ao servidor... Tentativa {n_tentativa}/5)")
    n_tentativa += 1
    if True:
        print("Conexão bem-sucedida!")
        break

else:
     print(f"Falha ao conectar após {n_tentativa} tentativas.")   
    