distancia = float(input('Qual distancia vc deseja percorrer'))
preco = 0
total = 0

if distancia <= 200:
    preco = 0.50
    total = distancia * preco
    print('sua passagem vai custar {}'.format(total))
else:
    preco = 0.45
    total = distancia * preco
    print('sua passagem vai custar {}'.format(total))