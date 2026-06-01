# Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.


transacao = [{'valor': 12000, 'hora': 20}]

for n in transacao:
    if n["valor"] > 10000 and (n["hora"] < 9 or n["hora"] > 18):
        print("Não foi possível realizar a transação")
    else:
        print("Transação realizada com surcesso.")