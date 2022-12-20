class Coffeemachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550
        self.start_coffee_machine()

    def start_coffee_machine(self):
        menu1 = "Write action(buy, fill, take, remaining, exit): "
        choice = None

        while choice != "exit":
            choice = input(menu1).strip()

            if choice == "buy":
                self.buy_menu()
                ...
            elif choice == "fill":
                self.fill_menu()
                ...
            elif choice == "take":
                self.take()
                ...
            elif choice == "remaining":
                self.remaining()
                ...
            ...
        ...

    def buy_menu(self):
        back = False

        while not back:
            msg = "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: "
            choice = input(msg).strip()

            if choice == "back":
                back = True

            elif choice.isdigit():
                int_choice = int(choice)
                if 0 < int_choice <= 3:
                    self.get_coffee(int_choice)
                    back = True
                    ...
                ...
            ...
        ...

    def get_coffee(self, choice: int):
        ing_list = self.get_ing_count(choice)
        drink_names = ["espresso", "latte", "cappuccino"]

        if self.check_ing(ing_list):
            self.water -= ing_list[0]
            self.milk -= ing_list[1]
            self.coffee_beans -= ing_list[2]
            self.money += ing_list[3]
            self.cups -= 1
            print("I have enough resources, making you a {0}!".format(drink_names[choice-1]))
        ...

    def check_ing(self, ing_list: list):
        if self.water < ing_list[0]:
            print("Sorry, not enough water")
            return False
        elif self.milk < ing_list[1]:
            print("Sorry, not enough milk")
            return False
        elif self.coffee_beans < ing_list[2]:
            print("Sorry, not enough coffee beans")
            return False
        elif self.cups < 1:
            print("Sorry, not enough cups")
            return False
        return True

    @staticmethod
    def get_ing_count(choice: int):
        list_ing = [0, 0, 0, 0]
        # Ingredient indexes: 0 - water, 1 - milk, 2 - coffee beans, 3 - money
        if choice == 1:
            list_ing[0] = 250
            list_ing[2] = 16
            list_ing[3] = 4
            ...
        elif choice == 2:
            list_ing[0] = 350
            list_ing[1] = 75
            list_ing[2] = 20
            list_ing[3] = 7
            ...
        else:
            list_ing[0] = 200
            list_ing[1] = 100
            list_ing[2] = 12
            list_ing[3] = 6
            ...
        return list_ing

    def fill_menu(self):
        ing = int(input("Write how many ml of water you want to add: "))
        self.water += ing

        ing = int(input("Write how many ml of milk you want to add: "))
        self.milk += ing

        ing = int(input("Write how many grams of coffee beans you want to add: "))
        self.coffee_beans += ing

        ing = int(input("Write how many disposable coffee cups you want to add: "))
        self.cups += ing
        ...

    def take(self):
        print(f"I gave you {self.money}")
        self.money = 0
        self.remaining()
        ...

    def remaining(self):
        print("The coffee machine has: \n{0} of water \n{1} of milk "
              "\n{2} of coffee beans \n{3} of disposable cups \n{4} of money\n"
              .format(self.water, self.milk, self.coffee_beans, self.cups, self.money))
        ...
    ...


cm = Coffeemachine()
