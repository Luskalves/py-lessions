def is_valid_triangle(sideA, sideB, sideC):
    if (sideA + sideB < sideC):
        return False
    elif (sideA + sideC < sideB):
        return False
    elif (sideB + sideC < sideA):
        return False
    else:
        return True


def is_triangle(sideA, sideB, sideC):
    is_valid = is_valid_triangle(sideA, sideB, sideC)
    print(is_valid)
    if (is_valid):
        if (sideA == sideB and sideB == sideC):
            return "Equilátero"
        elif (
                sideA == sideB and sideB != sideC
                or
                sideA != sideB and sideB == sideC
                or
                sideA != sideB and sideA == sideC
             ):
            return "Isóceles"
        else:
            return "Escaleno"
    else:
        return "Não é um triângulo."


ladoA = int(input("Digite o taqmnaho do lado A: "))
ladoB = int(input("Digite o taqmnaho do lado B: "))
ladoC = int(input("Digite o taqmnaho do lado C: "))

print(is_triangle(ladoA, ladoB, ladoC))
