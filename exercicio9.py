from utils import new_prompt

# Exercicio jogo limite de soma
new_prompt('Exercicio - limite da soma')
Soma = 0
Tentativas = 0
while Tentativas <= 20 and Soma < 50:
    Valor = int(input(f'Tentativa {Tentativas}. Digite um numero: '))
    if not Valor%2:
        Soma = Soma + Valor
    Tentativas += 1
else:
    print(f'Limite de tentativas, a soma foi {Soma}')

print(f'Final de jogo, a soma foi {Soma}')
