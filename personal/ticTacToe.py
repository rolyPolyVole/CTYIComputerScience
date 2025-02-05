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


def test_passes(iterable: list, predicate) -> int:
    passes = 0

    for e in iterable:
        if predicate(e):
            passes += 1

    return passes


def get_threat_coord(line: list[(str | None, (int, int))], player: str) -> (int, int):
    line_without_coords = list(map(lambda e: e[0], line))

    has_two_of_same = test_passes(line_without_coords, lambda e: e == player) == 2
    has_one_empty = test_passes(line_without_coords, lambda e: e is None) == 1

    if has_two_of_same and has_one_empty:
        return line[line_without_coords.index(None)][1]

    return None


def get_threat_possibility_coord(line: list[(str | None, (int, int))]) -> (int, int):
    line_without_coords = list(map(lambda e: e[0], line))

    has_o = test_passes(line_without_coords, lambda e: e == "O")
    has_two_empty = test_passes(line_without_coords, lambda e: e is None) == 2

    if has_o and has_two_empty:
        return line[line_without_coords.index(None)][1]


class TicTacToe:
    def __init__(self, smart: bool):
        self.smart = smart
        self.row1 = [None, None, None]
        self.row2 = [None, None, None]
        self.row3 = [None, None, None]
        self.rows = [self.row1, self.row2, self.row3]
        self.move = 0

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

            if self.smart:
                self.choose_smart_move()
            else:
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
        self.move += 1

    def choose_random_move(self):
        x = random.choice([0, 1, 2])
        y = random.choice([0, 1, 2])

        if self.rows[y][x] is not None:
            return self.choose_random_move()

        self.rows[y][x] = "O"
        self.move += 1

    def choose_smart_move(self):
        if self.move == 1:
            if self.rows[1][1] is not None:
                self.rows[2][2] = "O"  # Go corner
            else:
                self.rows[1][1] = "O"  # Go center

            self.move += 1
            return

        own_threat = self.find_threat("O")
        if own_threat is not None:
            self.rows[own_threat[0]][own_threat[1]] = "O"
            self.move += 1
            return

        other_threat = self.find_threat("X")
        if other_threat is not None:
            self.rows[other_threat[0]][other_threat[1]] = "O"
            self.move += 1
            return

        possible_threat = self.find_threat_possibility()
        if possible_threat is not None:
            self.rows[possible_threat[0]][possible_threat[1]] = "O"
            self.move += 1
            return

        self.choose_random_move()

    def find_threat(self, player: str) -> (int, int):
        lines = self.get_all_lines_with_coordinates()

        for line in lines:
            coord = get_threat_coord(line, player)

            if coord is not None:
                return coord

        return None

    def find_threat_possibility(self) -> (int, int):
        lines = self.get_all_lines_with_coordinates()

        for line in lines:
            coord = get_threat_possibility_coord(line)

            if coord is not None:
                return coord

        return None

    def check_winner(self) -> bool:
        lines = self.get_all_lines()

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
        if self.move == 9:
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("Game was a draw!")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            return True

        return False

    def get_all_lines_with_coordinates(self) -> list[list[(str | None, (int, int))]]:
        row_1 = list(map(lambda e: (e, (0, self.row1.index(e))), self.row1))
        row_2 = list(map(lambda e: (e, (1, self.row2.index(e))), self.row2))
        row_3 = list(map(lambda e: (e, (2, self.row3.index(e))), self.row3))
        col_1 = [(self.row1[0], (0, 0)), (self.row2[0], (1, 0)), (self.row3[0], (2, 0))]
        col_2 = [(self.row1[1], (0, 1)), (self.row2[1], (1, 1)), (self.row3[1], (2, 1))]
        col_3 = [(self.row1[2], (0, 2)), (self.row2[2], (1, 2)), (self.row3[2], (2, 2))]
        dia_1 = [(self.row1[0], (0, 0)), (self.row2[1], (1, 1)), (self.row3[2], (2, 2))]
        dia_2 = [(self.row1[2], (0, 2)), (self.row2[1], (1, 1)), (self.row3[0], (2, 0))]

        return [row_1, row_2, row_3, col_1, col_2, col_3, dia_1, dia_2]

    def get_all_lines(self) -> list[list[str | None]]:
        return list(map(lambda l: list(map(lambda e: e[0], l)), self.get_all_lines_with_coordinates()))


TicTacToe(True).start_game_cycle()
