'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.'''

#Programa:

km = int(input('Quantos km foram percorridos? '))
dias = int(input('Por quantos dias ele foi alugado? '))

preco = 60 * dias + 0.15 * km
print('\n Km = {}. Dias:{}'.format(km, dias))#\n é apenas p/ cria um espeço entre as pergunta e a resposta.
print('Valor a ser pago R$:{}'.format(preco))
