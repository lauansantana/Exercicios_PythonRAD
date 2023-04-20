#A fábrica de refrigerantes Meia-Cola vende seu produto em três formatos: lata de 350 ml, garrafa de 600 ml e garrafa de 2 litros. Se um comerciante compra uma determinada quantidade de cada formato, faça um algoritmo para calcular quantos litros de refrigerante ele comprou. 


qtd_latas = int(input('Informe a quantas latas de 350mlforam compradas: '))
qtd_garrafa600 = int(input('Informe a quantas garrafas de 600ml foram compradas: '))
qtd_garrafa2l = int(input('Informe a quantas garrafas de 2L foram compradas: '))

quantidade_total = (qtd_latas*350.0+qtd_garrafa600*600.0+qtd_garrafa2l*2000.0)/1000
print('Você comprou um total de {}L de refrigerante'.format(quantidade_total))