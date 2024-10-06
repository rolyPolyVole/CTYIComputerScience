

import random

print("Hello world")
print("Generating map...")

game_map = []

rows = 10
columns = 9


def generate_monster_map():
    for i in range(rows):
        game_map.append(generate_row(i))


def format_map():
    for row in game_map:
        string = ""
        for e in row:
            if e == " ":
                string = string + "◯ "
            else:
                string = string + "❌"
        print(string)


def has_monster_in_column(index):
    for row in game_map:
        if row[index] == "X":
            return True
    return False


def generate_row(index):
    if index == 0 or index == rows - 1:
        arr = []
        for i in range(columns):
            arr.append(" ")
        return arr
    else:
        arr = []
        has_monster = False

        for i in range(columns):
            arr.append(" ")
        while not has_monster:
            rand = random.randint(0, columns - 1)

            if not has_monster_in_column(rand):
                has_monster = True
                arr[rand] = "X"
        return arr


generate_monster_map()
format_map()

class Turbo:
    def __init__(self):
        return self
    def move_left(self):
        if self.x == 0:
            print("Error: Cannot move outside of the left wall!")
        else:
            self.x -= 1
    def move_right(self):
        if self.x == columns:
            print("Error: Cannot move outside of the right wall!")
        else:
            self.x += 1
    def move_down(self):
        if self.x == 0:
            print("You win!")
        else:
            self.y -= 1
    def move_up(self):
        if self.y == rows:
            print("Error: Cannot move above the height limit!")
        else:
            self.y += 1
    def check_walked_onto_monster(self):
        return game_map[rows - self.y][self.x] == "X"

    x = 0
    y = rows
    deaths = 0

# your algorithm goes here!
turbo = Turbo.__init__();+


def attempt(attempt_num):

