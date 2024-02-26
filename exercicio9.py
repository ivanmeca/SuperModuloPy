import random
from utils import new_prompt

# Exercicio jogo limite de soma
new_prompt('Exercicio - limite da soma')
Soma = 0
Tentativas = 0
while Tentativas <= 10 and Soma < 50:
    Soma += int(input(f'Tentativa {Tentativas}. Digite um numero: '))
    Tentativas += 1
    if Soma >= 50:
        print(f'Limite de soma atingida, a soma foi {Soma}')
        break
else:
    print(f'Limite de tentativas, a soma foi {Soma}')

print(f'Final de jogo')