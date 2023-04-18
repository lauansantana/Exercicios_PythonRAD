#8. Faça um algoritmo para ler três notas de um aluno em uma disciplina e imprimir a sua média ponderada (as notas tem pesos respectivos de 1, 2 e 3).

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))

media = (nota1*1)+(nota2*2)+(nota3*3)/6
print('A sua média ponderada é: ', media)