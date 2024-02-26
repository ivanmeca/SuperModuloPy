import random
import sys


def new_prompt(prompt):
    input('Pressione ENTER para continuar')
    for _ in range(100):
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
new_prompt('Exercicio - jogo')
NumeroAlvo = int(random.uniform(0, 100))
N_Tentativas = 0
Tentativa = 0
Limites = [0, 100]
while N_Tentativas <= 10:
    Tentativa = int(input(f'Tentativa {N_Tentativas}, o numero está entre {Limites[0]} e '
                          f'{Limites[1]}. Digite um numero: '))
    if Tentativa == NumeroAlvo:
        print('Parabens, você acertou!!')
        break
    if Tentativa > NumeroAlvo:
        print('O número é menor')
        Limites[1] = Tentativa
    else:
        print('O número é maior')
        Limites[0] = Tentativa
    N_Tentativas += 1
else:
    print(f'Limite de tentativas, o numero era {NumeroAlvo}')
print(f'Final de jogo')