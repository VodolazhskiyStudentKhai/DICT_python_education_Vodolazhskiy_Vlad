import random


class Dominoes:
    __stock_pieces = []
    __plr_pieces = []
    __comp_pieces = []
    __domino_snake = []
    __plr_turn: bool = False

    def __init__(self):
        for i in range(7):
            for j in range(7):
                if [j, i] in self.__stock_pieces:
                    continue
                self.__stock_pieces.append([i, j])
            ...
        self.find_snake()
    ...

    def distribute_pieces(self):
        for i in range(7):
            rand_el1 = random.choice(self.__stock_pieces)
            self.__stock_pieces.remove(rand_el1)
            self.__plr_pieces.append(rand_el1)
            rand_el1 = random.choice(self.__stock_pieces)
            self.__stock_pieces.remove(rand_el1)
            self.__comp_pieces.append(rand_el1)
            ...

    def find_snake(self):
        while len(self.__domino_snake) == 0:
            self.distribute_pieces()

            for i in range(len(self.__plr_pieces)):
                if [i, i] in self.__plr_pieces:
                    self.__plr_pieces.remove([i, i])
                    self.__domino_snake.append([i, i])
                    self.__plr_turn = False
                    break
                elif [i, i] in self.__comp_pieces:
                    self.__comp_pieces.remove([i, i])
                    self.__domino_snake.append([i, i])
                    self.__plr_turn = True
                    break
                ...

    def get_plr_turn(self):
        return self.__plr_turn

    def get_plr_pieces_str(self):
        print("Your pieces:")
        for i in range(len(self.__plr_pieces)):
            print(f"{i+1}: {self.__plr_pieces[i]}")
        ...

    def get_who_turn(self):
        return "player" if self.__plr_turn else "computer"

    def get_snake(self):
        return self.__domino_snake

    def get_plr_pieces(self):
        return self.__plr_pieces

    def get_comp_pieces(self):
        return self.__comp_pieces

    def get_stock(self):
        return self.__stock_pieces

    def switch_plr(self):
        self.__plr_turn = False if self.__plr_turn else True


class Interface:
    game: Dominoes = None

    def __init__(self, g: Dominoes):
        self.game = g

    def print_game_status(self):
        print(f"Stock size: {len(self.game.get_stock())}")
        print(f"Computer pieces: {len(self.game.get_comp_pieces())}\n")
        self.print_snake()
        self.game.get_plr_pieces_str()
        if self.game.get_who_turn() == "player":
            print("Status: It's your turn to make a move. Enter your command.")
        else:
            print("Status: Computer is about to make a move. Press Enter to continue...")
        ...

    def start_game(self):
        status = self.check_game_status()

        while status == 0:
            self.next_move()
            status = self.check_game_status()
        self.print_snake()

    def check_game_status(self):
        player = self.game.get_plr_pieces()
        computer = self.game.get_comp_pieces()
        snake: list = self.game.get_snake()
        stock = self.game.get_stock()
        move = self.game.get_who_turn()
        mess = 0

        if len(player) == 0:
            mess = "The game is over. You won!"
        elif len(computer) == 0:
            mess = "The game is over. The computer won!"
        elif snake[0][0] == snake[-1][-1]:
            score = 0
            for i in range(len(snake)):
                for s in snake[i]:
                    if s == snake[0][0]:
                        score += 1
            if score == 8:
                mess = "The game is over. It's a draw!"

        elif len(stock) == 0:
            mess = "The game is over. You won!" if move == "player" else "The game is over. The computer won!"

        team = player if move == "player" else computer
        if not Interface.team_can_move(team, snake[0], snake[-1]):
            self.game.switch_plr()
            mess = "The game is over. You won!" if self.game.get_plr_turn() else "The game is over. The computer won!"

        if mess != 0:
            print(mess)
        return mess

    def next_move(self):
        turn_plr = self.game.get_plr_turn()
        if turn_plr:
            self.print_game_status()

            el = int(input())
            ln = len(self.game.get_plr_pieces())

            if not -ln <= el <= ln:
                print("Invalid input. Please try again.")
                return

            if el >= 0:
                p1 = self.game.get_plr_pieces()[el-1]
                p2 = self.game.get_snake()[-1]
                if not Interface.check_pieces(p1, p2, False):
                    print("Illegal move. Please try again.")
                    return
                self.game.get_snake().append(p1)
            else:
                p1 = self.game.get_plr_pieces()[-el - 1]
                p2 = self.game.get_snake()[0]
                if not Interface.check_pieces(p1, p2, True):
                    print("Illegal move. Please try again.")
                    return
                self.game.get_snake().insert(0, p1)
            self.game.get_plr_pieces().remove(p1)
        else:
            self.comp_move()

        self.game.switch_plr()
    ...

    def comp_move(self):
        el = self.computer_sort()
        if el >= 0:
            p1 = self.game.get_comp_pieces()[el]
            self.game.get_snake().append(self.game.get_comp_pieces()[el])
        else:
            el *= -1
            p1 = self.game.get_comp_pieces()[el]
            self.game.get_snake().insert(0, self.game.get_comp_pieces()[el])
        self.game.get_comp_pieces().remove(p1)
        ...

    def computer_sort(self):
        all_pieces = self.game.get_comp_pieces().copy()
        all_pieces.extend(self.game.get_snake())
        values = {}

        for i in range(len(all_pieces)):
            for j in range(len(all_pieces[i])):
                val = values.get(all_pieces[i][j], 0)
                values[all_pieces[i][j]] = val + 1
                ...
            ...
        values_list = []
        comp_pieces = self.game.get_comp_pieces()
        for i in range(len(comp_pieces)):
            values_list.append(values.get(comp_pieces[i][0]) + values.get(comp_pieces[i][-1]))

        for i in range(len(comp_pieces)):
            index = values_list.index(max(values_list))

            p2l = self.game.get_snake()[0]
            p2r = self.game.get_snake()[-1]
            if self.check_pieces(comp_pieces[index], p2l, True):
                return -index
            elif self.check_pieces(comp_pieces[index], p2r, False):
                return index
            values_list[index] = 0

    @staticmethod
    def team_can_move(team: list, peace1: list, peace2: list):
        for i in range(len(team)):
            if Interface.check_pieces(team[i], peace1, True) or Interface.check_pieces(team[i], peace2, False):
                return True
        return False

    @staticmethod
    def check_pieces(piece1: list, piece2: list, left: bool):
        s = 0 if left else -1
        if piece2[s] not in piece1:
            return False
        else:
            if (piece1[0] == piece2[s] and left and piece1[-1] != piece2[s]) or\
                    (piece1[-1] == piece2[s] and not left and piece1[0] != piece2[s]):
                piece1.reverse()
        return True

    def print_snake(self):
        snake = self.game.get_snake()
        mess = str(snake) if len(snake) <= 6 else f"{snake[0:3]} ... {snake[-3:]}"
        print(mess)


game = Dominoes()
inter = Interface(game)
inter.start_game()
