from dice import Dice


class Player:
    def __init__(self, name, quantity_dices=4, turns=100000, games=7):
        self.__results = {}
        self.__results["wins"] = 0
        self.__results["lose"] = 0
        self.__results["draw"] = 0
        self.__results["name"] = name
        self.__results["information"] = Dice(
            turns, quantity_dices, games
        ).generate_dices()
        self.__results["quantity_dices"] = quantity_dices
        self.__results["turns"] = turns
        self.__results["games"] = games
        self.__results["results"] = []
        self.make_sum_of_dices()

    def victory(self):
        self.__results["wins"] += 1

    def lose(self):
        self.__results["lose"] += 1

    def draw(self):
        self.__results["draw"] += 1

    def get_information(self):
        return self.__results

    def get_results(self, number):
        return self.__results["results"][number]

    def make_sum_of_dices(self):
        for game in range(0, self.__results["games"]):
            for turn in range(0, self.__results["turns"]):
                soma = 0
                for dice in range(1, self.__results["quantity_dices"] + 1):
                    soma += self.__results["information"]["dices"][dice][turn][game]
                self.__results["results"].append(soma)
