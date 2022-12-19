bot_name = "Chatty"
year_create = 2022


def welcome(name, year):
    ...
    str_hello = "Hello! My name is %s. " \
                "\nI was created in %d"

    print(str_hello % (name, year))
    ask_name()
    ...


def ask_name():
    ...
    great_name = "What a great name you have, {0}!"

    name = input("Please, remind me your name.\n> ")
    print(great_name.format(name))
    get_age()
    ...


def get_age():
    ...
    str_age = "Let me guess your age." \
              "\nEnter remainders of dividing your age by 3, 5 and 7."
    answer_age = "Your age is {0}; that's a good time to start programming!"

    print(str_age)
    remainder3 = int(input("> "))
    remainder5 = int(input("> "))
    remainder7 = int(input("> "))

    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(answer_age.format(age))
    get_count()
    ...


def get_count():
    ...
    str_age = "Now I will prove to you that I can count to any number you want."
    print(str_age)
    count = int(input("> "))

    for num in range(count + 1):
        print("%d!" % num)
        ...
    get_last_answer()
    ...


def get_last_answer():
    ...
    str_question = "Let's test your programming knowledge." \
                   "\nWhat programming language stores code in the '.py' format?" \
                   "\n1. Java" \
                   "\n2. C++" \
                   "\n3. Python" \
                   "\n4. Udav" \
                   "\n5. Anaconda"

    str_try_again = "Please, try again."

    str_end = "Completed, have a nice day! " \
              "\nCongratulations, have a nice day!"

    print(str_question)
    answer = int(input("> "))

    while answer != 3:
        print(str_try_again)
        answer = int(input("> "))
        ...
    print(str_end)
    ...


welcome(bot_name, year_create)
