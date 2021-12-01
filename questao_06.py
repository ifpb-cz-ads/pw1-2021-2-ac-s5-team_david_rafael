valor_casa = float(input('Qual o valor da casa'))
salario = float(input('Qual o seu salario'))
anos = int(input('Quantos anos vc vai parcelar'))
meses = anos * 12
prestacao = valor_casa / meses
condicao = 30/100 * salario

print('serão {} parcelas no valor de {}'.format(meses, prestacao))

if prestacao > condicao:
    print('Seu emprestimo nao foi aprovado')
else:
    print('Seu emprestimo foi aprovado')