num1 = int(input('qual o primeiro numero'))
num2 = int(input('qual o segundo numero'))
resultado = 0

print('1 para: somar')
print('2 para: subtrair')
print('3 para: dividir')
print('4 para: multiplicar')
acao = int(input('oque vc deseja fazer'))

if acao == 1:
    resultado = num1 + num2
    print('a soma dos numeros é {}'.format(resultado))

if acao == 2:
    resultado = num1 - num2
    print('a subtracao dos numeros é {}'.format(resultado))

if acao == 3:
    resultado = num1 / num2
    print('a divisao dos numeros é {}'.format(resultado))

if acao == 4:
    resultado = num1 * num2
    print('a multiplicacao dos numeros é {}'.format(resultado))