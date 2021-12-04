num1 = int(input('informe o primeiro numero'))
num2 = int(input('informe o segundo numero'))
num3 =int(input('informe o terceiro numero'))

maior = 0
menor = 0

if num1 < num2 and num1 < num3:
    menor = num1
elif num1 > num2 and num1 > num3:
        maior = num1
if num2 < num1 and num2 < num3:
    menor = num2
elif num2 > num1 and num2 > num3:
    maior = num2
if num3 < num1 and num3 < num2:
    menor = num3
elif num3 > num1 and num3 > num2:
    maior = num3

print('esse é o maior numero {} e esse é o menor {}'.format(maior, menor))