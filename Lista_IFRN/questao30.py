#30. Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um algoritmo que receba o salário fixo de um funcionário e o valor de suas vendas, calcule e mostre a comissão e o salário final do funcionário. 

salario = float(input('Informe o valor do seu salário: '))
valor_vendas = float(input('Informe o valor das vendas: '))
comissao = 4*valor_vendas/100
print('Comissao: R${}\nSalário final: R${}'.format(comissao, salario+comissao))