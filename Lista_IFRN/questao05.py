#5. Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.

preco_litro = float(input('Informe o preço da gasolina: '))
valor_pago = float(input('Informe o valor pago: '))
tanque = valor_pago/preco_litro

print('Você colocou {:.2f}L no tanque.'.format(tanque))
