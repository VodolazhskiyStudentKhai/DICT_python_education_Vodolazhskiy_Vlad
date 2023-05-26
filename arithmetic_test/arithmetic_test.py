import random


class Arithmetictest:
    @staticmethod
    def start_test(max_quests):
        close = False
        true_answers = 0
        level = None

        while not close:
            level = input("Which level do you want? Enter a number:"
                          "\n1 - simple operations with numbers 2-9"
                          "\n2 - integral squares of 11-29"
                          "\n3 - square root of 30-99"
                          "\n>")

            if not level.isdigit():
                print("Wrong format! Try again.")
                continue

            for i in range(max_quests):
                result = Arithmetictest.get_quest(int(level))
                if result is None:
                    print("Incorrect format.")
                    break
                if Arithmetictest.check_result(result):
                    true_answers += 1
                    ...
                close = True
                ...
            ...
        Arithmetictest.choose_save(true_answers, max_quests, level)

    @staticmethod
    def get_quest(difficult: int):
        result = None
        match difficult:
            case 1:
                result = Arithmetictest.quest1()
            case 2:
                rand = random.randint(11, 29)
                result = rand ** 2
                print(rand)
            case 3:
                result = random.randint(30, 99)
                answer = result ** 2
                print(answer)
        return result

    @staticmethod
    def quest1():
        first = random.randint(2, 9)
        second = random.randint(2, 9)
        quest = random.randint(1, 3)
        result = None
        operation = ""

        match quest:
            case 1:
                result = first * second
                operation = "*"
            case 2:
                result = first + second
                operation = "+"
            case 3:
                result = first - second
                operation = "-"
                ...
        print(f"{first} {operation} {second}")
        return result

    @staticmethod
    def check_result(result: int):
        answer = input(">")

        if answer.isdigit():
            answer = int(answer)
            if result == answer:
                print("Right!")
                return True

        print("Wrong!")
        return False

    @staticmethod
    def choose_save(true_answers, max_quests, level):
        answer = input(f"Your mark is {true_answers}/{max_quests}. "
                       f"Would you like to save the result? Enter yes or no.\n>").strip().lower()

        if answer == "yes" or answer == "y":
            name = input("What is your name?\n>")
            with open("results.txt", 'w', encoding="utf-8") as file:
                file.write(f"{name}: {true_answers}/{max_quests} in level {level}")


Arithmetictest.start_test(5)
