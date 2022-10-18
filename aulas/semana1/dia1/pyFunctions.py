# def imc(peso: int, altura: int) -> float:
#   return peso / (altura / 100) ** 2


# print(f"sem parametros: {imc(55, 182):.2f}")
# print(f"Com parametros: {imc(peso=55, altura=182):.2f}")


def concat(*strings):
    final_string = ""
    for string in strings:
        final_string += string
        if not string == strings[-1]:
            final_string += ", "
    return final_string


print(concat("Carlos", "Cristina"))

concat("Carlos", "Creistina", "Maria")

dict(nome="Felipe", sobrenome="Silvia", idade=25)

dict(nome="Ana", sobrenome="Souza", idade=21, turma=1)
