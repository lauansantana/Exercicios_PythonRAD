#Uma fábrica controla o tempo de trabalho sem acidentes pela quantidade de dias. Faça um algoritmo para converter este tempo em anos, meses e dias. Assuma que cada mês possui sempre 30 dias.

dias = int(input('Informe a quantidade de dias: '))

ano = dias/365
mes = dias/30

print('Conversao em Anos: {:.2f}\nMeses: {}\n'.format(ano, mes))
