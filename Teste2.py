# Exercicio 01
# valor1 = int(input('Digite um valor inteiro:'))
# valor2 = int(input('Digite um segundo valor inteiro:'))
# print(f'A soma entre {valor1} e {valor2} é de {valor1+valor2}')

# Exercicio 02
# notas = []
# media = 0
# for x in range(10):
#     notas.append(int(input('Digite um valor')))
#     media += notas[x]
#
# print(f'A media é {media / 4}')

# Exercicio 03
# dimensoes = []
# for x in ['Altura','Largura']:
#     dimensoes.append(int(input(f'Digite a {x}: ')))
#
# area = dimensoes[0] * dimensoes[1]
# print(f'A área  é {area}, seu dobro é {area*2}')

# Exercicio 04
valorHora = float(input('Informe seu valor recebido por hora: '))
TotalHoras = float(input('Qauntas horas trabalhou no mês: '))

print(f'Seu salário nesse mês será de: R${valorHora*TotalHoras:.2f}')
