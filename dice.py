import numpy as np


class Dice:
    def __init__(self, turns=100000, quantity=4, games=7):
        self.__result = {}
        self.__result["quantity"] = quantity
        self.__result["turns"] = turns
        self.__result["games"] = games
        self.__result["dices"] = {}
        self.__result["dices"]["one"] = 0
        self.__result["dices"]["two"] = 0
        self.__result["dices"]["three"] = 0
        self.__result["dices"]["four"] = 0
        self.__result["dices"]["five"] = 0
        self.__result["dices"]["six"] = 0

    def generate_numbers(self):
        lista = np.random.randint(
            1, 7, size=(self.__result["turns"], self.__result["games"])
        )
        return lista

    def generate_dices(self):
        quantity = self.__result["quantity"]
        while quantity != 0:
            self.__result["dices"][quantity] = self.generate_numbers()
            quantity -= 1
        self.generate_information()
        return self.__result

    def generate_information(self):
        quantity = self.__result["quantity"]
        while quantity != 0:
            self.__result["dices"]["one"] += (
                self.__result["dices"][quantity] == 1
            ).sum()
            self.__result["dices"]["two"] += (
                self.__result["dices"][quantity] == 2
            ).sum()
            self.__result["dices"]["three"] += (
                self.__result["dices"][quantity] == 3
            ).sum()
            self.__result["dices"]["four"] += (
                self.__result["dices"][quantity] == 4
            ).sum()
            self.__result["dices"]["five"] += (
                self.__result["dices"][quantity] == 5
            ).sum()
            self.__result["dices"]["six"] += (
                self.__result["dices"][quantity] == 6
            ).sum()
            quantity -= 1
