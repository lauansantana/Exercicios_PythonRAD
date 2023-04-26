'''31. Faça um algoritmo que receba o peso de uma pessoa, calcule e mostre:
a) o novo peso se a pessoa engordar 15% sobre o peso digitado;
b) o novo peso se a pessoa emagrecer 20% sobre o peso digitado.'''

peso = float(input('Informe o seu peso: '))
engordar = 15*peso/100
emagrecer = 20*peso/100
print('Peso se você engordar 15%: {}\nPeso se você emagrecer 20%: {}'.format(peso+engordar, peso-emagrecer))
