#A granja Frangotech possui um controle automatizado de cada frango da sua produção. No pé direito do frango há um anel com um chip de identificação; no pé esquerdo são dois anéis para indicar o tipo de alimento que ele deve consumir. Sabendo que o anel com chip custa R$4,00 e o anel de alimento custa R$3,50, faça um algo ritmo para calcular o gasto total da granja para marcar todos os seus frangos. 

frango = int(input('Informe q quantidade de frangos a serem marcados: '))
gasto = 3.50*2+4
print('Para marcar {} frangos, será gasto R$ {}'.format(frango,frango*gasto))