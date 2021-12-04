vel = float(input('Qual a velocidade do carro?' ))
multa = 0

if vel > 80:
    multa = (vel - 80) * 5
    print('vc ultrapassou os limites e sua multa é de {}'.format(multa))
else:
    print('vc esta dentro do limite de velocidade')