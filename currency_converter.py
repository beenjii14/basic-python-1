menu = """
Bienvenido al conversor de monedas 🤑

1.- Pesos Mexicanos
2.- Pesos Colombianos
3.- Pesos Argentinos

Elige una opción: """

while True:
    option = int(input(menu))
    if option > 0 and option < 4:
        break

valueDollar = {
    '1': 20.13,
    '2': 3844,
    '3': 98.39
}

while True:
    pesos = float(input('¿Cuantos pesos tienes? '))
    if pesos > 0:
        dollars = round(pesos / valueDollar[str(option)], 2)
        print(f'Tienes ${dollars} dolares')
        break
