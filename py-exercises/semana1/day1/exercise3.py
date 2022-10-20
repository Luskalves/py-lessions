def square_art(n):
    if (n > 1):
        for line in range(n):
            print("*"*n)


size = int(input("Digite a quantidade de '*' na tela: "))
square_art(size)
