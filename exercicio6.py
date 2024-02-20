def NewPrompt(prompt):
    input('Pressione ENTER para continuar')
    for x in range(100):
        print('\n')
    print(prompt)


# Exercicio
# NewPrompt('Exercio - teste de valor')
# valor = float(input('Informe um valor: '))
# if valor >= 0:
#     print(f'{valor} é positivo')
# else:
#     print(f'{valor} é negativo')

# Exercicio
# NewPrompt('Exercio - teste de valor string')
# valor = input('Informe o Sexo (M/F):')
# if valor.lower() == 'm' :
#     print(f'Masculino')
# elif valor.lower() == 'f':
#     print(f'Feminino')
# else:
#     print(f'Inválido')

# Exercicio
# NewPrompt('Exercio - teste de vogal em string')
# valor = input('Digite uma letra:')
#
# if len(valor) > 1:
#     print(f'O valor digitado contem mais de uma letra, considerando "{valor[0]}" para o teste')
#
# if valor[0].lower() in ['a','e','i','o','u']:
#     print(f'{valor[0]} é uma vogal')
# else:
#     print(f'{valor[0]} é uma consoante')

# Exercicio
# NewPrompt('Exercio - Notas do aluno')
# valor = float(input('Digite a primeira nota:'))
# valor2 = float(input('Digite a segunda nota:'))
#
# media = (valor + valor2) / 2
#
# if media >= 7.0:
#     print(f'A média do aluno foi {media}, ele foi aprovado!')
# else:
#     print(f'A média do aluno foi {media}, ele foi reprovado!')


# Exercicio
NewPrompt('Exercio - produto mais barato')

escolha = 0
valorEscolha = 0
for x in range(3):
    preco = float(input(f'Digite o valor do produto {x+1}: '))
    if valorEscolha == 0:
        escolha = x+1
        valorEscolha = preco
    elif preco <= valorEscolha:
        escolha = x+1
        valorEscolha = preco

print(f'O produto mais barato é o produto {escolha}')
