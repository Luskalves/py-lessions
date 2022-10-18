restaurants = [
    {"name": "Restaurante A", "nota": 4.5},
    {"name": "Restaurante B", "nota": 3.0},
    {"name": "Restaurante C", "nota": 4.2},
    {"name": "Restaurante D", "nota": 2.3},
]

filtered_restaurants = []
min_rating = 3.0

# for restaurant in restaurants:
#     if restaurant["nota"] > min_rating:
#         filtered_restaurants.append(restaurant["nota"])

filtered_restaurants = [
    restaurant for restaurant in restaurants if restaurant["nota"] > min_rating
]

print(filtered_restaurants)

quadrados = [x * x for x in range(11)]

print(quadrados)


languages = ["Python", "Java", "Javascript"]

enumerate_prime = enumerate(languages)

print(list(enumerate_prime))

for index, language in enumerate(["Pytho", "Java"]):
    print(f"{index} - {language}")


# gods = [
#   { 'Nome': 'Whyanna', 'Domínio': 'Magia' },
#   { 'Nome': 'Nimb', 'Domínio': 'Sorte' },
#   { 'Nome': 'Ahadarak', 'Domínio': 'Tormenta' }
# ]

# domains = [god['Domínio'] for god in gods if god['Domínio']]

# not_evil_domains = [
#                     god["Domínio"] for god in gods 
#                     if god["Domínio"] != "Tormenta"
# ]

# evil_domains = [god['Domínio'] for god in gods
# if god['Domínio'] == 'Tormenta']

# print(f"Todos os domínios: {domains}")
# print(f"Todos os domínios do bem: {not_evil_domains}")
# print(f"Todos os domínios malignos: {evil_domains}")
