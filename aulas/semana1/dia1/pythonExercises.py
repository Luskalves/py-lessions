# exercise 12

number = int(input("Digite um valor: "))

result = 1

for num in range(number):
    result += num * result

print(result)

# exercise 13

lista = [6, 8, 5, 9, 10]

rating_list = [n * 10 for n in lista]

print(rating_list)

# exercise 14

for multiple in rating_list:
    if multiple % 3 == 0:
        print(f"{multiple} é multiplo de 3")
