#24. Um tonel de refresco é feito com 8 partes de água mineral e 2 partes de suco de maracujá. Faça um algoritmo para calcular quantos litros de água e de suco são necessários para se fazer X litros de refresco (informados pelo usuário). 

quantidade = float(input('Informe quantos litros de refresco será feito: '))
suco = quantidade%8
agua = quantidade-suco

print('Para fazer {}L de refresco, será necessário {}L de água e {}L de maracujá.'.format(quantidade, agua, suco))
