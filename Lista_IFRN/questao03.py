#3. A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia. Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com base nestes fatos, faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular os dados solicitados.


pao = int(input('Informe a quantidade de paes: '))
broa = int(input('Informe a quantidade de broas: '))

pao_total = pao*0.12
broa_total = broa*1.50
total_arrecadado = pao_total+broa_total

print('O total de pae e broas arrecadado foi: R$ {}'.format(total_arrecadado))
print('Você deve guardar numa conta poupança R$ {}a (10% do total arrecadado)'.format(10*total_arrecadado/100))
