#A empresa Hipotheticus paga R$10,00 por hora normal trabalhada, e R$15,00 por hora extra. Faça um algoritmo para calcular e imprimir o salário bruto e o salário líquido de um determinado funcionário. Considere que o salário líquido é igual ao salário bruto descontando-se 10% de impostos.

hora = float(input('Informe as horas trabalhadas: '))
hora_extra = float(input('Informe as horas extras trabalhadas: '))

salario_bruto = 10*hora + 15*hora_extra
desconto = 10*salario_bruto/100
salario_liquido = salario_bruto-desconto
print('Salário bruto: R${}\nSalário líquido: R${}'.format(salario_bruto, salario_liquido))