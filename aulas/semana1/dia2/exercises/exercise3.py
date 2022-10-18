aprovados = []

with open('exercise3.txt', mode='r') as file:
    for line in file:
        note = line.split(" ")
        if (int(note[1]) >= 6):
            aprovados.append(note)

with open('aprovados.txt', mode='w') as new_file:
    for aprovado in aprovados:
        new_file.writelines(f"{aprovado[0]}\n")
