from utils import new_prompt

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
Soma = 0
for x in range(10):
    valor = int(input(f'Tentativa {x}. Digite um numero: '))
    if not valor % 6:
        Soma += valor
    if Soma >= 30:
        break
print(f'Final de jogo, a soma foi {Soma}')
