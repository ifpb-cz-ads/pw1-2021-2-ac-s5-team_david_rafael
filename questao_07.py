faixa = float(input('Quantos kWh são consumidos: '))
print('agora informe o tipo de instalacao')
print('')
print('R para residencia')
print('I para industria')
print ('C para comercio')
preco = 0

acao = str(input('Qual o tipo de instalacao? '))

if acao == 'R':
    if faixa <= 500:
        preco = faixa * 0.40
    else:
        preco = faixa * 0.65
    print('Voce vai pagar {}'.format(preco))

if acao == 'C':
    if faixa <= 1000:
        preco = faixa * 0.55
    else:
        preco = faixa * 0.60
    print('Voce vai pagar {}'.format(preco))

if acao == 'R':
    if faixa <= 5000:
        preco = faixa * 0.55
    else:
        preco = faixa * 0.60
    print('Voce vai pagar {}'.format(preco))

