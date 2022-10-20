notas = [7, 6, 8, 7]


def media(notas):
    total = 0
    for nota in notas:
        total += nota

    avg = total / len(notas)
    return avg


avg = media(notas)

print(f"media: {avg}")
