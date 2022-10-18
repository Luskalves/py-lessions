eu_literalmente = ["Coringa (2019)\n", "Scarface\n"]

try:
    with open("literalmente_eu.txt", mode="w") as file:
        file.write("Patrick Bateman\n")
        file.write("Batman (Robert Pattinson)\n")
        file.write("Agente K\n")
        file.write("Driver\n")
        print("Ikari Shinji", file=file)
        file.writelines(eu_literalmente)
except TypeError:
    print('Erro de tipo ao abrir o arquivo!')
except FileNotFoundError:
    print("Falha ao criar o arquivo!")
except ValueError:
    print("Falha ao escolher o modo de leitura/escrita")
else:
    print('Escrita ocorreu bem!')

try:
    with open("literalmente_eu.txt", mode="r") as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print("Falha ao tentar ler o arquivo! inexistente/não encontrado")
else:
    print("Leitura ocorreu com sucesso!")

finally:
    print("Programa finalizado.")
