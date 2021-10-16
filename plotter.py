from game import Game
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self):
        self.__result = {}
        self.__result["game"] = Game().get_information()

    def plot_player_dices(self, player):
        plt.figure(clear=True)
        dices = self.__result["game"]["information"][player]["information"]["dices"]
        player_dices = plt
        sides = list(range(1, 7))
        values = [
            dices["one"],
            dices["two"],
            dices["three"],
            dices["four"],
            dices["five"],
            dices["six"],
        ]
        player_dices.bar(sides, values)
        for i, j in zip(sides, values):
            player_dices.annotate(str(j), xy=(i, j))
        player_dices.suptitle("Informações dos dados do " + player)
        player_dices.savefig("plot_" + player + "_dices.png")
        player_dices.show()

    def plot_all_game_result(self):
        plt.figure(clear=True)
        possible = list(range(4, 25))
        media = 0
        elementos = 0
        results = []
        for number in range(4, 25):
            number_results = self.__result["game"]["information"]["player_one"][
                "results"
            ].count(number)
            number_results += self.__result["game"]["information"]["player_two"][
                "results"
            ].count(number)
            elementos += number_results
            results.append(number_results)
            media += number_results * number
        media = media / elementos
        print("Media:" + str(media))
        all_game_result = plt
        all_game_result.bar(possible, results)
        for i, j in zip(possible, results):
            all_game_result.annotate(str(j), xy=(i, j))
        all_game_result.suptitle("Informações sobre o resultado de todos os jogos")
        all_game_result.savefig("plot_all_game_result.png")
        all_game_result.show()

    def plot_pair_odd(self, player):
        pair_odd = plt
        pair_odd.figure(clear=True)
        pair = 0
        odd = 0
        for dice in range(1, 5):
            pair += (
                self.__result["game"]["information"][player]["information"]["dices"][
                    dice
                ]
                % 2
                == 0
            ).sum()
            odd += (
                self.__result["game"]["information"][player]["information"]["dices"][
                    dice
                ]
                % 2
                == 1
            ).sum()
        values = [pair, odd]
        for i, j in zip([0, 1], values):
            pair_odd.annotate(str(j), xy=(i, j))
        pair_odd.bar(["par", "ímpar"], values)
        pair_odd.suptitle("Ocorrência de pares e ímpares nos dados do " + player)
        pair_odd.savefig("pair_odd" + player + ".png")
        pair_odd.show()

    def results_only(self, player, principal, secondary, secondary2):
        wins_only = plt
        wins_only.figure(clear=True)
        wins = self.__result["game"]["information"][player][principal]
        lose_draw = (
            self.__result["game"]["information"][player][secondary]
            + self.__result["game"]["information"][player][secondary2]
        )
        values = [wins, lose_draw]
        wins_only.bar([principal, str(secondary + "-" + secondary2)], values)
        for i, j in zip([principal, str(secondary + "-" + secondary2)], values):
            wins_only.annotate(str(j), xy=(i, j))
        wins_only.suptitle(principal + " VS " + secondary + "-" + secondary2)
        wins_only.savefig(principal + "_only_player_one.png")
        wins_only.show()

    def main(self):
        while True:
            print(
                """
            1 - Ver resultados dos dados do jogador um
            2 - Ver resultados dos dados do jogador dois
            3 - Ver resultado das somas de todos os jogos
            4 - Ver números pares dos dados do jogador um
            5 - Ver números pares dos dados do jogador dois
            6 - Ver vitórias X derrotas e empates do jogador um
            7 - Ver derrotas X vitórias e empates do jogador um
            8 - Ver empates X vitórias e derrotas do jogador um
            9 - Sair
            escolha: """
            )
            choices = int(input())

            if choices == 1:
                self.plot_player_dices("player_one")
            else:
                if choices == 2:
                    self.plot_player_dices("player_two")
                else:
                    if choices == 3:
                        self.plot_all_game_result()
                    else:
                        if choices == 4:
                            self.plot_pair_odd("player_one")
                        else:
                            if choices == 5:
                                self.plot_pair_odd("player_two")
                            else:
                                if choices == 6:
                                    self.results_only(
                                        "player_one", "wins", "lose", "draw"
                                    )
                                else:
                                    if choices == 7:
                                        self.results_only(
                                            "player_one", "lose", "wins", "draw"
                                        )
                                    else:
                                        if choices == 8:
                                            self.results_only(
                                                "player_one", "draw", "wins", "lose"
                                            )
                                        else:
                                            if choices == 9:
                                                exit()


simulator = Plotter()
simulator.main()
