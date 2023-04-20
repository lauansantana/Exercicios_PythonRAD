#Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar. Faça um algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, em reais. Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real. Não havendo moeda de um tipo, a quantidade respectiva é zero.

moeda1cent = int(input('Informe quantas moedas de 1 Centavo você possui: '))
moeda5cent = int(input('Informe quantas moedas de 5 Centavos você possui: '))
moeda10cent = int(input('Informe quantas moedas de 10 Centavos você possui: '))
moeda25cent = int(input('Informe quantas moedas de 25 Centavos você possui: '))
moeda50cent = int(input('Informe quantas Moedas de 50 centavos você possui: '))
moeda1real = int(input('Informe quantas moedas de 1 Real você possui: '))

total=(moeda1cent*0.01)+(moeda50cent*0.05)+(moeda10cent*0.10)+(moeda25cent*0.25)+(moeda50cent*0.50)+(moeda1real*1)
print('Você conseguiu poupar R${:.2f}'.format(total))