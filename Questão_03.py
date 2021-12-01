salario = float(input('qual o seu salaraio'))
aumento = 0

if salario > 1250:
    aumento = (10/100 * salario)
    salario = salario + aumento
    print('voce recebeu um aumento de {} totalizando em {}'.format(aumento, salario))
else:
    aumento = (15/100 * salario)
    salario = salario + aumento
    print('voce recebeu um aumento de {} totalizando em {}'.format(aumento, salario))