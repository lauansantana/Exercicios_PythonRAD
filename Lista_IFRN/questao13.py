'''13. Ler um número inteiro (assuma até três dígitos) e imprimir a saída da seguinte forma:
CENTENA = x
DEZENA = x
UNIDADE = x'''


n1 = int(input('Insira um número (até 3 dígitos)'))
unidade = n1%10
n1 = n1-unidade/10
dezena = n1/10
centena = n1/100
dezena = int(dezena)
centena = int(centena)
print('CENTENA: {}\nDEZENA: {}\nUNIDADE: {}'.format(centena, dezena, unidade))