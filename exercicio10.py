from utils import new_prompt

# Exercicio Soma de multiplos
new_prompt('Exercicio - soma dos multiplos')
Soma = 0
for x in range(10):
    valor = int(input(f'Tentativa {x}. Digite um numero: '))
    if not valor % 6:
        Soma += valor
    if Soma >= 30:
        break
print(f'Final de jogo, a soma foi {Soma}')
