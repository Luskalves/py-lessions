eu_literalmente = ['Coringa (2019)\n', 'Scarface\n']

with open('literalmente_eu.txt', mode='w') as file:
    file.write('Patrick Bateman\n')
    file.write('Batman (Robert Pattinson)\n')
    file.write('Agente K\n')
    file.write('Driver\n')
    print('Ikari Shinji', file=file)
    file.writelines(eu_literalmente)

with open('literalmente_eu.txt', mode="r") as file:
    for line in file:
        print(line)
