import re

nome = input('Digite um valor inteiro:')
idade = input('Digite sua idade:')
cpf = input('Digite seu CPF:')
cpfMask = re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}')
match = cpfMask.match(cpf)

print(f'Olá {nome}\nSeus dados cadastrados foram: Idade = {idade} e CPF = {cpf}')



