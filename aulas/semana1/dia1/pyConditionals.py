# Menor que R$2.000,00, pessoa desenvolvedora estagiária;

# Entre R$2.000,00 e R$5.800,00, pessoa desenvolvedora júnior;

# Entre R$5.800,00 e R$7.500,00, pessoa desenvolvedora pleno;

# Entre R$7.500,00 e R$10.500,00, pessoa desenvolvedora sênior;

# Qualquer valor acima do que já foi mencionado a pessoa desenvolvedora é considerada liderança.a

salario = int(input("Digite o valor do salário: "))
position = ""

if salario < 2000:
    position = "Estagiário"

elif 2000 <= salario < 5800:
    position = "Desenvolvedor Júnior"

elif 5800 <= salario < 7500:
    position = "Desenvolvedor Pleno"

elif 7500 <= salario < 10500:
    position = "Desenvolvedor Sênior"

else:
    position = "Pessoa Desenvolvedora Lider"

print(f"A pessoa recebe {salario} e está no cargo de {position}")


