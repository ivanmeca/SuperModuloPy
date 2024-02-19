# Exercicio 04
valorHora = float(input('Informe seu valor recebido por hora: '))
TotalHoras = float(input('Qauntas horas trabalhou no mês: '))

bruto = valorHora*TotalHoras
inss = bruto * 0.08
irpf = bruto * 0.11
sindicato = bruto * 0.05

print(f'Seu salário bruto nesse mês será de: R${valorHora*TotalHoras:.2f}')
print(f'Seu inss nesse mês será de: R${inss:.2f}')
print(f'Seu irpf nesse mês será de: R${irpf:.2f}')
print(f'Sua contribuição sindical nesse mês será de: R${sindicato:.2f}')
print(f'Seu salário liquido será de: R${bruto-inss-irpf-sindicato:.2f}')
