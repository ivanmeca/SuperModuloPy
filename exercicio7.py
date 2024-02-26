import random


def NewPrompt(prompt):
    input('Pressione ENTER para continuar')
    for x in range(100):
        print('\n')
    print(prompt)


# Exercicio
# NewPrompt('Exercicio - numeros pares')
# x = 0
# while x <= 10:
#     if not (x % 2):
#         print(x)
#     x += 1

# Exercicio jogo de adivinhação
NewPrompt('Exercicio - jogo')
numeroAlvo = int(random.uniform(0, 100))
n_tentativas = 0
tentativa = 0
limites = [0,100]
while n_tentativas <= 10:
    tentativa = int(input(f'Tentativa {n_tentativas}, o numero está entre {limites[0]} e {limites[1]}. Digite um numero: '))
    if tentativa == numeroAlvo:
        print('Parabens, você acertou!!')
        exit(0)
    if tentativa > numeroAlvo:
        print('O número é menor')
        limites[1] = tentativa
    else:
        print('O número é maior')
        limites[0] = tentativa
    n_tentativas += 1

print(f'O numero era {numeroAlvo}')
