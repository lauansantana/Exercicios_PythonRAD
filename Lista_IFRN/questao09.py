#9. Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina informe quanto será o valor arrecadado.


quantidade_pequena = int(input('Informe a quantidade de camisetas pequenas: '))
quantidade_media = int(input('Informe a quantidade de camisetas médias: '))
quantidade_prande = int(input('Informe a quantidade de camisetas grandes: '))

valor_arrecadado = (quantidade_pequena*10)+(quantidade_media*12)+(quantidade_prande*15)
print('O valor arrecadado foi: {}'.format(valor_arrecadado))