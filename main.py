from games.blackjack import jugar_blackjack
from games.craps import jugar_craps
from games.ruleta import jugar_ruleta
from games.tragaperras import jugar_tragaperras

usuarios = {}


def crear_cuenta():
    usuario = input("Crea un nombre de usuario: ").strip()

    if usuario in usuarios:
        print("Ese usuario ya existe.")
        return None

    contraseña = input("Crea una contraseña: ").strip()

    usuarios[usuario] = {
        "contraseña": contraseña,
        "fichas": 100
    }

    print(f"Cuenta creada. {usuario} tiene 100 fichas.")
    return usuario


def iniciar_sesion():
    usuario = input("Nombre de usuario: ").strip()

    if usuario not in usuarios:
        print("Ese usuario no existe.")
        return None

    contraseña = input("Contraseña: ").strip()

    if usuarios[usuario]["contraseña"] != contraseña:
        print("Contraseña incorrecta.")
        return None

    return usuario


def login():

    while True:

        print("\n=== INICIO ===")
        print("1. Iniciar sesión")
        print("2. Crear cuenta")
        print("3. Salir")

        opcion = input("> ").strip()

        if opcion == "1":

            usuario = iniciar_sesion()

            if usuario:
                return usuario

        elif opcion == "2":

            usuario = crear_cuenta()

            if usuario:
                return usuario

        elif opcion == "3":
            return None

        else:
            print("Opción no válida.")


def menu(usuario):

    while True:

        fichas = usuarios[usuario]["fichas"]

        print("\n=== CASINO ===")
        print(f"Jugador: {usuario}")
        print(f"Fichas: {fichas}")

        print("1. Blackjack")
        print("2. Craps")
        print("3. Ruleta")
        print("4. Tragaperras")
        print("5. Cerrar sesión")
        print("6. Salir")

        opcion = input("> ").strip()

        if opcion == "1":
            usuarios[usuario]["fichas"] = jugar_blackjack(fichas)

        elif opcion == "2":
            usuarios[usuario]["fichas"] = jugar_craps(fichas)

        elif opcion == "3":
            usuarios[usuario]["fichas"] = jugar_ruleta(fichas)

        elif opcion == "4":
            usuarios[usuario]["fichas"] = jugar_tragaperras(fichas)

        elif opcion == "5":
            break

        elif opcion == "6":
            exit()

        else:
            print("Opción no válida.")


while True:

    usuario = login()

    if usuario is None:
        break

    menu(usuario)