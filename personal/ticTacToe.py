import random
import time

print("Hello World")

x_values = ["a", "b", "c"]
y_values = [3, 2, 1]


def validate_input(value: str) -> bool:
    if len(value) != 2:
        return False

    if not x_values.__contains__(value[0]):
        return False

    if not y_values.__contains__(int(value[1])):
        return False

    return True


def get_x(value: str):
    return x_values.index(value[0])


def get_y(value: str):
    return y_values.index(int(value[1]))


def test_all(iterable: list, predicate) -> bool:
    for e in iterable:
        if not predicate(e):
            return False

    return True


def test_any(iterable: list, predicate) -> bool:
    for e in iterable:
        if predicate(e):
            return True

    return False


class TicTacToe:
    def __init__(self):
        self.row1 = [None, None, None]
        self.row2 = [None, None, None]
        self.row3 = [None, None, None]
        self.rows = [self.row1, self.row2, self.row3]

        self.playing = False

    def start_game_cycle(self):
        self.playing = True
        print("The game has started!")

        while self.playing:
            time.sleep(1.5)

            self.print_board()
            self.ask_user_for_input()

            if self.check_winner():
                self.playing = False
                self.print_board()
                break

            self.print_board()

            time.sleep(1.5)
            print("The computer is making a move!")
            time.sleep(1.5)

            self.choose_random_move()

            if self.check_winner():
                self.playing = False
                self.print_board()
                break

    def print_board(self):
        row_texts = ["3 ", "2 ", "1 ", "  a b c"]

        i = 0
        for row in self.rows:
            for e in row:
                row_texts[i] += "-" if e is None else e
                row_texts[i] += " "

            i += 1

        print(row_texts[0] + "\n" + row_texts[1] + "\n" + row_texts[2] + "\n" + row_texts[3])

    def ask_user_for_input(self):
        user_input = input("Give a coordinate (e.g. a1, b3)\n>>> ")

        if not validate_input(user_input):
            print("Invalid Input!")
            return self.ask_user_for_input()

        x = get_x(user_input)
        y = get_y(user_input)

        if self.rows[y][x] is not None:
            print("There's already something there!")
            return self.ask_user_for_input()

        self.rows[y][x] = "X"

    def choose_random_move(self):
        x = random.choice([0, 1, 2])
        y = random.choice([0, 1, 2])

        if self.rows[y][x] is not None:
            return self.choose_random_move()

        self.rows[y][x] = "O"

    def check_winner(self) -> bool:
        row_1 = self.row1
        row_2 = self.row2
        row_3 = self.row3
        col_1 = [self.row1[0], self.row2[0], self.row3[0]]
        col_2 = [self.row1[1], self.row2[1], self.row3[1]]
        col_3 = [self.row1[2], self.row2[2], self.row3[2]]
        dia_1 = [self.row1[0], self.row2[1], self.row3[2]]
        dia_2 = [self.row1[2], self.row2[1], self.row3[0]]

        lines = [row_1, row_2, row_3, col_1, col_2, col_3, dia_1, dia_2]
        is_full = test_all(self.rows, lambda r: test_all(r, lambda e: e is not None))

        if test_any(lines, lambda l: test_all(l, lambda e: e == "X")):
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("You win!")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            return True
        if test_any(lines, lambda l: test_all(l, lambda e: e == "O")):
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("You managed to lose to a random move algorithm!")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            return True
        if is_full:
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("Game was a draw!")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            return True
        
        return False


TicTacToe().start_game_cycle()
