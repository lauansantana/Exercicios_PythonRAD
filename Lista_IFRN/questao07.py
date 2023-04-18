#7. Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do ano. Esqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias.


mes = 30

dia = int(input('Informe o dia: '))
mes_entrada = int(input('Informe o mes: '))

if mes_entrada == 1:
    print('Se passaram {} dias desde o início do ano.'.format(dia))

if mes_entrada == 2:
    print('Se passaram {} dias desde o início do ano.'.format(30+dia))

if mes_entrada == 3:
    print('Se passaram {} dias desde o início do ano.'.format(60+dia))

if mes_entrada == 4:
    print('Se passaram {} dias desde o início do ano.'.format(90+dia))

if mes_entrada == 5:
    print('Se passaram {} dias desde o início do ano.'.format(120+dia))

if mes_entrada == 6:
    print('Se passaram {} dias desde o início do ano.'.format(150+dia))

if mes_entrada == 7:
    print('Se passaram {} dias desde o início do ano.'.format(180+dia))

if mes_entrada == 8:
    print('Se passaram {} dias desde o início do ano.'.format(210+dia))

if mes_entrada == 9:
    print('Se passaram {} dias desde o início do ano.'.format(240+dia))

if mes_entrada == 10:
    print('Se passaram {} dias desde o início do ano.'.format(270+dia))

if mes_entrada == 11:
    print('Se passaram {} dias desde o início do ano.'.format(300+dia))

if mes_entrada == 12:
    print('Se passaram {} dias desde o início do ano.'.format(330+dia))
