import random


mazo = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
        "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
        "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
        "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
STARTING_CHIPS = 100


def PuntDealer(mazoDealer):
    PuntDealer = 0
    for i in range(len(mazoDealer)):
        if mazoDealer[i] == "J" or mazoDealer[i] == "Q" or mazoDealer[i] == "K":
            PuntDealer += 10
        else:
            PuntDealer += mazoDealer[i]
    return PuntDealer


def PuntJugador(mazoJugador):
    puntJuga = 0
    for i in range(len(mazoJugador)):
        if mazoJugador[i] == "J" or mazoJugador[i] == "Q" or mazoJugador[i] == "K":
            puntJuga += 10
        else:
            puntJuga += mazoJugador[i]
    return puntJuga


def shuffle():
    mazoBarajado = mazo.copy()
    random.shuffle(mazoBarajado)
    return mazoBarajado





def repartirJugador(mazoBarajado):
    print(len(mazoBarajado))
    mazoJugador = []
    mazoJugador.append(mazoBarajado[len(mazoBarajado) - 1])
    mazoBarajado.pop(len(mazoBarajado) - 1)
    mazoJugador.append(mazoBarajado[len(mazoBarajado) - 1])
    mazoBarajado.pop(len(mazoBarajado) - 1)
    puntJuga = PuntJugador(mazoJugador)
    print(mazoJugador)
    print(puntJuga)


def repartirDealer(mazoBarajado):
    mazoDealer = []
    mazoDealer.append(mazoBarajado[len(mazoBarajado) - 1])
    mazoBarajado.pop(len(mazoBarajado) - 1)
    print(len(mazoBarajado))
    print(mazoDealer)

def jugar():
    mazoBarajado = shuffle()
    repartirJugador(mazoBarajado)
    repartirDealer(mazoBarajado)
    print(repartirJugador)
    print(repartirDealer)

jugar()