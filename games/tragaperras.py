import random

simbolos = ["🍒", "🍋", "🔔", "⭐", "7"]


def girar_rodillos():
    resultado = [
        random.choice(simbolos),
        random.choice(simbolos),
        random.choice(simbolos)
    ]
    return resultado


def calcular_premio(resultado, apuesta):
    if resultado[0] == resultado[1] == resultado[2]:
        return apuesta * 5
    elif resultado[0] == resultado[1] or resultado[0] == resultado[2] or resultado[1] == resultado[2]:
        return apuesta * 2
    else:
        return 0


def jugar_tragaperras(fichas):

    print("Bienvenido a la Tragaperras")
    print(f"Tienes {fichas} fichas")

    while fichas > 0:
        print()
        apuesta = int(input("Introduce tu apuesta: "))

        if apuesta <= 0:
            print("La apuesta debe ser mayor que 0.")
            continue

        if apuesta > fichas:
            print("No tienes suficientes fichas.")
            continue

        fichas -= apuesta

        resultado = girar_rodillos()
        print(" | ".join(resultado))

        premio = calcular_premio(resultado, apuesta)

        if premio > 0:
            fichas += premio
            print(f"Has ganado {premio} fichas.")
        else:
            print("No has ganado nada.")

        print(f"Fichas actuales: {fichas}")

        seguir = input("¿Quieres seguir jugando? (s/n): ").lower()

        if seguir != "s":
            break

    print("Gracias por jugar a la tragaperras.")

    return fichas