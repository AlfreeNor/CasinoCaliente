import random
from typing import Dict, List, Optional, Tuple


WHEEL: List[int] = [
    0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27,
    13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1,
    20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26,
]

RED_NUMBERS = {
    1, 3, 5, 7, 9, 12, 14, 16, 18,
    19, 21, 23, 25, 27, 30, 32, 34, 36,
}
BLACK_NUMBERS = {
    2, 4, 6, 8, 10, 11, 13, 15, 17,
    20, 22, 24, 26, 28, 29, 31, 33, 35,
}

class RouletteGame:
    def __init__(self, fichas) -> None:
        self.chips = fichas

    @staticmethod
    def get_color(number: int) -> str:
        if number == 0:
            return "verde"
        if number in RED_NUMBERS:
            return "rojo"
        return "negro"

    @staticmethod
    def spin_wheel() -> int:
        return random.choice(WHEEL)

    def show_rules(self) -> None:
        print("\nRULETA")
        print("Tipos de apuesta disponibles:")
        print("  1. Numero")
        print("  2. Color")
        print("  3. Paridad")
        print("  4. Docena")
        print("  5. Mitad")

    def ask_bet_amount(self) -> int:
        while True:
            amount_text = input(f"\n¿Cuántas fichas quieres apostar? (Saldo: {self.chips}) > ").strip()
            if not amount_text.isdigit():
                print("Introduce un número válido.")
                continue
            amount = int(amount_text)
            if amount <= 0:
                print("La apuesta debe ser mayor que 0.")
                continue
            if amount > self.chips:
                print("No tienes suficientes fichas.")
                continue
            return amount

    def ask_bet_type(self) -> Tuple[str, object]:
        while True:
            print("\nElige tipo de apuesta:")
            print("  numero | color | paridad | docena | mitad")
            bet_type = input("> ").strip().lower()

            if bet_type == "numero":
                number_text = input("Elige un número entre 0 y 36 -> ").strip()
                if number_text.isdigit() and 0 <= int(number_text) <= 36:
                    return bet_type, int(number_text)
                print("Número no válido.")

            elif bet_type == "color":
                color = input("Elige rojo o negro -> ").strip().lower()
                if color in {"rojo", "negro"}:
                    return bet_type, color
                print("Color no válido.")

            elif bet_type == "paridad":
                parity = input("Elige par o impar -> ").strip().lower()
                if parity in {"par", "impar"}:
                    return bet_type, parity
                print("Opción no válida.")

            elif bet_type == "docena":
                dozen_text = input("Elige 1 (1-12), 2 (13-24) o 3 (25-36) -> ").strip()
                if dozen_text in {"1", "2", "3"}:
                    return bet_type, int(dozen_text)
                print("Docena no válida.")

            elif bet_type == "mitad":
                half = input("Elige baja (1-18) o alta (19-36) -> ").strip().lower()
                if half in {"baja", "alta"}:
                    return bet_type, half
                print("Opción no válida.")

            else:
                print("Tipo de apuesta no válido.")

    def evaluate_bet(self, bet_type: str, selection: object, amount: int, result: int) -> Tuple[bool, int]:
        won = False
        payout = 0

        if bet_type == "numero":
            if result == selection:
                won = True
                payout = amount * 35

        elif bet_type == "color":
            if result != 0 and self.get_color(result) == selection:
                won = True
                payout = amount

        elif bet_type == "paridad":
            if result != 0:
                if selection == "par" and result % 2 == 0:
                    won = True
                    payout = amount
                elif selection == "impar" and result % 2 == 1:
                    won = True
                    payout = amount

        elif bet_type == "docena":
            if result != 0:
                if selection == 1 and 1 <= result <= 12:
                    won = True
                    payout = amount * 2
                elif selection == 2 and 13 <= result <= 24:
                    won = True
                    payout = amount * 2
                elif selection == 3 and 25 <= result <= 36:
                    won = True
                    payout = amount * 2

        elif bet_type == "mitad":
            if result != 0:
                if selection == "baja" and 1 <= result <= 18:
                    won = True
                    payout = amount
                elif selection == "alta" and 19 <= result <= 36:
                    won = True
                    payout = amount

        return won, payout

    def play_round(self) -> bool:
        print("\n" + "-" * 40)
        amount = self.ask_bet_amount()
        bet_type, selection = self.ask_bet_type()

        self.chips -= amount
        result = self.spin_wheel()
        color = self.get_color(result)

        print("\nLa bola está girando...")
        print(f"Resultado: {result} ({color})")

        won, payout = self.evaluate_bet(bet_type, selection, amount, result)
        if won:
            self.chips += amount + payout
            print(f"¡Ganaste! Beneficio: {payout} fichas.")
        else:
            print("Has perdido la apuesta.")

        print(f"Saldo actual: {self.chips} fichas")

        if self.chips <= 0:
            print("\nTe has quedado sin fichas. Fin de la partida.")
            return False

        while True:
            again = input("¿Quieres seguir jugando? (s/n) -> ").strip().lower()
            if again in {"s", "si", "sí"}:
                return True
            if again in {"n", "no"}:
                return False
            print("Respuesta no válida.")

    def run(self) -> int:
        self.show_rules()
        while self.play_round():
            pass
        print("\nGracias por jugar.")
        return self.chips

def jugar_ruleta(fichas):
    game = RouletteGame(fichas)
    return game.run()       