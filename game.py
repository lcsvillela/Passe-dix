from player import Player


class Game:
    def __init__(
        self,
        name_player_one="Player One",
        name_player_two="Player Two",
        turns=100000,
        games=1,
        quantity_dices=4,
    ):
        self.__results = {}
        self.__results["player_one"] = Player(
            name_player_one, quantity_dices, turns, games
        )
        self.__results["player_two"] = Player(
            name_player_two, quantity_dices, turns, games
        )
        self.__results["information"] = {}
        self.__results["turns"] = turns
        self.game_results()

    def game_results(self):
        for turn in range(0, self.__results["turns"]):
            result_player_one = self.__results["player_one"].get_results(turn)
            result_player_two = self.__results["player_two"].get_results(turn)
            self.who_wins(result_player_one, result_player_two)
        self.__results["information"]["player_one"] = self.__results[
            "player_one"
        ].get_information()
        self.__results["information"]["player_two"] = self.__results[
            "player_two"
        ].get_information()

    def get_information(self):
        return self.__results

    def who_wins(self, player_one, player_two):
        if player_one == 13 and player_two == 13:
            self.__results["player_one"].draw()
            self.__results["player_two"].draw()
        else:
            if player_one == 13:
                self.__results["player_one"].victory()
                self.__results["player_two"].lose()
            else:
                if player_two == 13:
                    self.__results["player_one"].lose()
                    self.__results["player_two"].victory()
