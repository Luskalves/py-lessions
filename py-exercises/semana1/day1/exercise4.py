names = ['luska', 'baggyr', 'pambo', 'lare']


def bigger_name(list):
    new_list = sorted(list, key=len)
    print(new_list)
    return new_list[-1]


print(bigger_name(names))
