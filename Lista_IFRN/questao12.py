#Faça um algoritmo para ler o salário de um funcionário e aumentá-Io em 15%. Após o aumento, desconte 8% de impostos. Imprima o salário incial, o salário com aumento e o salário final.

salario = float(input('Informe o Seu salário: '))

aumento = (15*salario)/100
desconto = (8*salario)/100

print('Salario inicial: {}\nSalário com aumento: {}\nSalário com final: {}'.format(salario,salario+aumento,salario-desconto))