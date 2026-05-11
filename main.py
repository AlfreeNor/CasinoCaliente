from games.blackjack import jugar_blackjack
from games.craps import jugar_craps
from games.ruleta import jugar_ruleta
from games.tragaperras import jugar_tragaperras
from database.supabase_client import crear_usuario, iniciar_usuario, actualizar_fichas, obtener_usuario


def crear_cuenta():
    usuario = input("Crea un nombre de usuario: ").strip()

    if usuario == "":
        print("El nombre de usuario no puede estar vacío.")
        return None

    contrasena = input("Crea una contraseña: ").strip()

    if contrasena == "":
        print("La contraseña no puede estar vacía.")
        return None

    nuevo_usuario = crear_usuario(usuario, contrasena)

    if nuevo_usuario is None:
        print("Ese usuario ya existe.")
        return None

    print(f"Cuenta creada. {usuario} tiene 100 fichas.")
    return nuevo_usuario


def iniciar_sesion():
    usuario = input("Nombre de usuario: ").strip()
    contrasena = input("Contraseña: ").strip()

    usuario_logueado = iniciar_usuario(usuario, contrasena)

    if usuario_logueado is None:
        print("Usuario o contraseña incorrectos.")
        return None

    return usuario_logueado


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


def guardar_fichas(usuario, fichas):
    actualizar_fichas(usuario["usuario"], fichas)
    usuario["fichas"] = fichas


def menu(usuario):
    while True:
        usuario_actualizado = obtener_usuario(usuario["usuario"])

        if usuario_actualizado is not None:
            usuario = usuario_actualizado

        fichas = usuario["fichas"]

        print("\n=== CASINO ===")
        print(f"Jugador: {usuario['usuario']}")
        print(f"Fichas: {fichas}")

        print("1. Blackjack")
        print("2. Craps")
        print("3. Ruleta")
        print("4. Tragaperras")
        print("5. Cerrar sesión")
        print("6. Salir")

        opcion = input("> ").strip()

        if opcion == "1":
            nuevas_fichas = jugar_blackjack(fichas)
            guardar_fichas(usuario, nuevas_fichas)

        elif opcion == "2":
            nuevas_fichas = jugar_craps(fichas)
            guardar_fichas(usuario, nuevas_fichas)

        elif opcion == "3":
            nuevas_fichas = jugar_ruleta(fichas)
            guardar_fichas(usuario, nuevas_fichas)

        elif opcion == "4":
            nuevas_fichas = jugar_tragaperras(fichas)
            guardar_fichas(usuario, nuevas_fichas)

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