import random
from typing import Tuple


class CrapsGame:
    def __init__(self, fichas) -> None:
        self.chips = fichas
        self.point = None

    @staticmethod
    def roll_dice() -> Tuple[int, int, int]:
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        total = die_1 + die_2
        return die_1, die_2, total

    def show_rules(self) -> None:
        print("\nCRAPS")
        print("\nTirada inicial, llamada come-out roll:")
        print("  - Si sale 7 u 11, ganas.")
        print("  - Si sale 2, 3 o 12, pierdes.")
        print("  - Si sale 4, 5, 6, 8, 9 o 10, ese número se convierte en el punto.")
        print("\nCuando hay punto:")
        print("  - Ganas si vuelve a salir el punto antes que el 7.")
        print("  - Pierdes si sale 7 antes que el punto.")

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

    @staticmethod
    def wait_for_roll() -> None:
        input("Pulsa Enter para tirar los dados...")

    def play_pass_line_round(self) -> None:
        amount = self.ask_bet_amount()
        self.chips -= amount
        self.point = None

        print("\nCOME-OUT ROLL")
        self.wait_for_roll()
        die_1, die_2, total = self.roll_dice()
        print(f"Has sacado {die_1} + {die_2} = {total}")

        if total in {7, 11}:
            winnings = amount
            self.chips += amount + winnings
            print(f"¡Natural! Has ganado {winnings} fichas.")
            return

        if total in {2, 3, 12}:
            print("Craps. Has perdido la apuesta.")
            return

        self.point = total
        print(f"El punto queda establecido en {self.point}.")
        print(f"Ahora necesitas sacar {self.point} antes que 7 para ganar.")

        while True:
            print("\nTIRADA DE PUNTO")
            self.wait_for_roll()
            die_1, die_2, total = self.roll_dice()
            print(f"Has sacado {die_1} + {die_2} = {total}")

            if total == self.point:
                winnings = amount
                self.chips += amount + winnings
                print(f"¡Has sacado el punto! Ganas {winnings} fichas.")
                self.point = None
                return

            if total == 7:
                print("Seven-out. Ha salido 7 antes que el punto. Pierdes la apuesta.")
                self.point = None
                return

            print("No ha salido ni el punto ni el 7. Se sigue tirando.")

    def ask_play_again(self) -> bool:
        if self.chips <= 0:
            print("\nTe has quedado sin fichas. Fin de la partida.")
            return False

        print(f"\nSaldo actual: {self.chips} fichas")

        while True:
            answer = input("¿Quieres jugar otra ronda? (s/n) > ").strip().lower()
            if answer in {"s", "si", "sí"}:
                return True
            if answer in {"n", "no"}:
                return False
            print("Respuesta no válida.")

    def run(self) -> int:
        self.show_rules()

        playing = True
        while playing:
            self.play_pass_line_round()
            playing = self.ask_play_again()

        print("\nGracias por jugar.")
        return self.chips


def jugar_craps(fichas):
    game = CrapsGame(fichas)
    return game.run()