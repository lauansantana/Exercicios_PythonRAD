#29. Faça um algoritmo que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%. 

produto = float(input('Informe o preço do produto'))
desconto = produto-(10*produto/100)
print('O novo preço é de {} com 10% de desconto'.format(desconto))
