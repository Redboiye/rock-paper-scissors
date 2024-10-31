from random import choice
import time


class Player:

    def __init__(self, nickname, is_npc=False, action=None):
        self.action = action
        self.is_npc = is_npc
        self.nickname = nickname

    @staticmethod
    def get_random_action():
        return choice(Game.POSSIBLE_ACTIONS)


class Game:
    game_is_running = True
    POSSIBLE_ACTIONS = ['scissors', 'paper', 'rock']
    BEATS = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    def __init__(self, player_1, player_2):
        self.player_wins = 0
        self.npc_wins = 0
        self.ties = 0
        self.player_1 = player_1
        self.player_2 = player_2
        self.start_game_round()
        # inits simbolize klases iekavas kad pasauc klasi un izveido objektu
        # def is metode

    def start_game_round(self):

        while self.game_is_running:
            print("GET READY BITCH!!")
            time.sleep(1)
            self.player_1.action = input(f"{self.player_1.nickname}, choose: s(scissors), p(paper), r(rock)!")
            if self.player_1.action == "s":
                self.player_1.action = "scissors"
                break
            elif self.player_1.action == "p":
                self.player_1.action = "paper"
                break
            elif self.player_1.action == "r":
                self.player_1.action = "rock"
                break
            else:
                print("invalid! try again!")

        self.player_2.action = self.player_2.get_random_action()

        print(f"{self.player_2.nickname} choose: {self.player_2.action}")

        result = self.check_winner(self.player_1, self.player_2)
        print(result)

        self.play_again()

    def play_again(self):

        while True:
            restart = input("Do you want to play again? 'y' or 'n': ")
            if restart == 'y':
                self.start_game_round()
                break
            elif restart == 'n':
                self.show_winner()
                exit("thanks for playing!")
            else:
                print("invalid! try again!")

    def check_winner(self, player_1: Player, player_2: Player):
        if player_1.action == player_2.action:
            self.ties += 1
            return "it's a tie"
        elif self.BEATS.get(player_1.action) == player_2.action:
            self.player_wins += 1
            return f"{player_1.nickname} wins with {player_1.action}!"
        else:
            self.npc_wins += 1
            return f"{player_2.nickname} wins with {player_2.action}!"

    def show_winner(self):
        print(
            f"Final_Score: '{self.player_1.nickname} WINS:{self.player_wins}',"
            f"'TIES:{self.ties}',"
            f" '{self.player_2.nickname} WINS:{self.npc_wins}'"
        )


print("Welcome to Rock-paper-scissors!")
player_1_nickname = input("Choose nickname:")
player_x = Player(nickname=player_1_nickname)
player_y = Player(nickname='npc', is_npc=True)

# klase ka funckcijas definicija ir blue print, kas notiek ja vinus pasauc.
Game(player_x, player_y)
