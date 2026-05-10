import random

mazo = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
        "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
        "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
        "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

def barajar_mazo():
    mazo_barajado = mazo.copy()
    random.shuffle(mazo_barajado)
    return mazo_barajado


def repartir_carta(mazo_barajado):
    return mazo_barajado.pop()


def calcular_puntos(mano):
    puntos = 0
    ases = 0

    for carta in mano:
        if carta == "J" or carta == "Q" or carta == "K":
            puntos += 10
        elif carta == "A":
            puntos += 11
            ases += 1
        else:
            puntos += carta

    while puntos > 21 and ases > 0:
        puntos -= 10
        ases -= 1

    return puntos


def mostrar_mano(nombre, mano):
    print(f"{nombre}: {mano} | Puntos: {calcular_puntos(mano)}")


def jugar_blackjack(fichas):
    mazo_barajado = barajar_mazo()

    mano_jugador = []
    mano_dealer = []

    mano_jugador.append(repartir_carta(mazo_barajado))
    mano_jugador.append(repartir_carta(mazo_barajado))

    mano_dealer.append(repartir_carta(mazo_barajado))
    mano_dealer.append(repartir_carta(mazo_barajado))

    print("Bienvenido al Blackjack")
    print(f"Fichas iniciales: {fichas}")
    print()

    mostrar_mano("Jugador", mano_jugador)
    print(f"Dealer: [{mano_dealer[0]}, ?]")
    print()

    while calcular_puntos(mano_jugador) < 21:
        opcion = input("¿Quieres pedir carta? (s/n): ").lower()

        if opcion == "s":
            nueva_carta = repartir_carta(mazo_barajado)
            mano_jugador.append(nueva_carta)
            print(f"Has recibido: {nueva_carta}")
            mostrar_mano("Jugador", mano_jugador)
        elif opcion == "n":
            break
        else:
            print("Opción no válida. Escribe s o n.")

    puntos_jugador = calcular_puntos(mano_jugador)

    if puntos_jugador > 21:
        print()
        print("Te has pasado de 21. Pierdes.")
        mostrar_mano("Jugador", mano_jugador)
        mostrar_mano("Dealer", mano_dealer)
        return fichas

    print()
    print("Turno del dealer")

    while calcular_puntos(mano_dealer) < 17:
        nueva_carta = repartir_carta(mazo_barajado)
        mano_dealer.append(nueva_carta)
        print(f"El dealer recibe: {nueva_carta}")

    puntos_dealer = calcular_puntos(mano_dealer)

    print()
    mostrar_mano("Jugador", mano_jugador)
    mostrar_mano("Dealer", mano_dealer)
    print()

    if puntos_dealer > 21:
        print("El dealer se ha pasado. Ganas.")
    elif puntos_jugador > puntos_dealer:
        print("Ganas.")
    elif puntos_jugador < puntos_dealer:
        print("Pierdes.")
    else:
        print("Empate.")

    return fichas