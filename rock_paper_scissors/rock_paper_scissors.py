import math
import random
import re


class RockPaperScissors:
    @staticmethod
    def start_game():
        ex = False
        name = input("Enter your name:>").strip()
        ratting = RockPaperScissors.get_score(name)
        print(f"Hello, {name}")

        opt = RockPaperScissors.set_options()

        while ex is False:
            comp_choice = random.choice(opt)
            plr_choice = input(">").strip().lower()
            match plr_choice:
                case "!exit":
                    print("Bye!")
                    ex = True
                case "!ratting":
                    print(f"Your ratting: {ratting}")
                case _:
                    if plr_choice not in opt:
                        print(f"Invalid input: {plr_choice}")
                    else:
                        ratting = RockPaperScissors.get_winner(plr_choice, comp_choice, ratting)
        ...

    @staticmethod
    def get_winner(plr_answer: str, comp_answer: str, ratting: int):
        options = RockPaperScissors.get_options_list()
        plr_i = options.index(plr_answer)
        comp_i = options.index(comp_answer)
        half = math.floor(len(options) / 2)

        if plr_i == comp_i:
            print(f"There is a draw ({comp_answer})")
            ratting += 50
        elif (plr_i > comp_i and plr_i - comp_i <= half) or not (plr_i < comp_i and comp_i - plr_i <= half):
            print(f"Well done. The computer chose {comp_answer} and failed")
            ratting += 100
        else:
            print(f"Sorry, but the computer chose {comp_answer}")

        return ratting

    @staticmethod
    def get_score(name: str):
        file = open("ratting.txt", 'r')
        ratting = 0
        for line in file:
            reg = r"^{0}\s".format(name)
            parse = re.match(reg + r"\d+", line)
            if parse is not None:
                parse_str = parse.group(0)
                ratting = int(re.split(reg, parse_str)[1])
                break
            ...
        return ratting

    @staticmethod
    def get_options_list():
        return ["fire", "rock", "gun", "lightning", "devil", "dragon", "water", "air", "paper", "sponge", "wolf",
                "tree", "human", "snake", "scissors"]

    @staticmethod
    def set_options():
        options = re.split(r",\s|,", input(">").strip().lower())
        full_list = RockPaperScissors.get_options_list()

        for o in options.copy():
            o = o.strip()
            if o not in full_list:
                print(f"Unknown param: {o}")
                options.remove(o)
                ...
            ...
        if len(options) == 0:
            options = ["rock", "paper", "scissors"]
            ...
        return options


RockPaperScissors.start_game()
