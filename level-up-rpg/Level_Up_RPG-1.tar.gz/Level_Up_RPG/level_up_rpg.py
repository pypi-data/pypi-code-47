"""
This file contains source code of the game "Level_Up_RPG".
Author: DtjiAppDev
"""


import sys
import random
sys.modules['_decimal'] = None
import decimal
from decimal import *
from decimal import Decimal

getcontext().Emin = -10 ** 10000
getcontext().Emax = 10 ** 10000
getcontext().traps[Overflow] = 0
getcontext().traps[Underflow] = 0
getcontext().traps[DivisionByZero] = 0
getcontext().traps[InvalidOperation] = 0
getcontext().prec = 100


class Player:
    """
    This class contains attributes of the player in the game.
    """

    def __init__(self, name: str) -> None:
        self.player_id: str = str(random.randint(1000000000, 9999999999))
        self.name: str = name
        self.level: int = 1
        self.curr_hp: Decimal = Decimal("115")
        self.max_hp: Decimal = Decimal("115")
        self.attack_power: Decimal = Decimal("25")

    def restore(self):
        # type: () -> None
        self.curr_hp = self.max_hp

    def level_up(self):
        # type: () -> None
        self.level += 1
        self.max_hp *= 2
        self.restore()
        self.attack_power *= 2

    def attack(self, target):
        # type: (Player or Enemy) -> None
        target.curr_hp -= self.attack_power

    def is_alive(self) -> bool:
        return self.curr_hp > 0

    def __str__(self):
        # type: () -> str
        res: str = ""  # initial value
        res += "ID: " + str(self.player_id) + "\n"
        res += "Name: " + str(self.name) + "\n"
        res += "Level: " + str(self.level) + "\n"
        res += "HP: " + str(self.curr_hp) + "/" + str(self.max_hp) + "\n"
        res += "Attack power: " + str(self.attack_power) + "\n"
        return res


class Enemy:
    """
    This class contains attributes of the enemy in the game.
    """

    def __init__(self) -> None:
        self.enemy_id: str = str(random.randint(1000000000, 9999999999))
        self.name: str = "COM"
        self.level: int = 1
        self.curr_hp: Decimal = Decimal("125")
        self.max_hp: Decimal = Decimal("125")
        self.attack_power: Decimal = Decimal("20")

    def restore(self):
        # type: () -> None
        self.curr_hp = self.max_hp

    def level_up(self):
        # type: () -> None
        self.level += 1
        self.max_hp *= 2
        self.restore()
        self.attack_power *= 2

    def attack(self, target):
        # type: (Player or Enemy) -> None
        target.curr_hp -= self.attack_power

    def is_alive(self) -> bool:
        return self.curr_hp > 0

    def __str__(self):
        # type: () -> str
        res: str = ""  # initial value
        res += "ID: " + str(self.enemy_id) + "\n"
        res += "Name: " + str(self.name) + "\n"
        res += "Level: " + str(self.level) + "\n"
        res += "HP: " + str(self.curr_hp) + "/" + str(self.max_hp) + "\n"
        res += "Attack power: " + str(self.attack_power) + "\n"
        return res


def main():
    """
    This function is used to run the game.
    :return: None
    """

    print("Welcome to Level_Up_RPG! In this game, you will play as long as you survive in this game.")
    print("This game is about levelling up as much as possible and going as far as possible.")
    name: str = input("Please enter your name: ")
    player: Player = Player(name)
    enemy: Enemy = Enemy()
    round_number: int = 1
    while True:
        print("-" * 160)
        print("ROUND " + str(round_number))
        print("Below are your current stats.\n" + str(player))
        print("Below are your enemy's current stats.\n" + str(enemy))
        print("Enter 1 to continue playing.")
        print("Enter 2 to quit.")
        option: str = input("Please enter a number: ")
        while not option.isnumeric() or int(option) < 1 or int(option) > 2:
            option = input("Sorry, invalid input! Please enter another number: ")

        if int(option) == 2:
            sys.exit()

        turn: int = 0
        while player.is_alive() and enemy.is_alive():
            turn += 1
            if turn % 2 == 1:
                print("It is your turn to attack.")
                player.attack(enemy)

            else:
                print("It is your enemy's turn to attack.")
                enemy.attack(player)

            print("Below are your current stats.\n" + str(player))
            print("Below are your enemy's current stats.\n" + str(enemy))

            if enemy.is_alive() and not player.is_alive():
                print("GAME OVER! " + str(player.name).capitalize() + " died.")
                sys.exit()

            if player.is_alive() and not enemy.is_alive():
                print("You won the battle.")

        for i in range(random.randint(1, 100)):
            player.level_up()

        for i in range(random.randint(1, 100)):
            enemy.level_up()

        round_number += 1


if __name__ == '__main__':
    main()
