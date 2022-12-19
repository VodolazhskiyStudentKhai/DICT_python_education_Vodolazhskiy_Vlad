import random


def welcome():
    welcome_msg = "Type 'play' to play the game, 'exit' to quit:>"
    inp = input(welcome_msg).strip()

    while inp != "play" and inp != "exit":
        inp = input(welcome_msg)

    if inp == "play":
        start_game()
    ...


def start_game():
    health = 8
    inp_str = "HANGMAN\n{0}\nInput a letter: > "
    sur_msg = "You guessed the word {0}!\nYou survived!"
    die_msg = "You lost!"
    not_cont = "That letter doesn't appear in the word"
    contain = "You've already guessed this letter"

    words_list = ["python", "java", "javascript", "php"]

    correct_word = random.choice(words_list)
    length = len(correct_word)
    blur_list = list("-" * length)

    while health > 0 and "-" in blur_list:
        blur = "".join(blur_list[:length])
        char = input(inp_str.format(blur)).strip()

        if check_letter(char) == 0:
            continue

        if char in blur_list:
            print(contain)

        elif char not in correct_word:
            health -= 1
            blur_list.append(char)
            print(not_cont)

        else:
            blur_list = change_list(blur_list, correct_word, char)
        ...
    msg = sur_msg.format(correct_word) if health > 0 else die_msg
    print(msg)
    ...


def check_letter(char):
    s_let = "You should input a single letter."
    low_eng = "Please enter a lowercase English letter."

    if len(char) != 1 or not char.isalpha():
        print(s_let)
        return 0

    if char.isascii() != 1 or char.islower() != 1:
        print(low_eng)
        return 0
    ...


def change_list(blur_list, word, c):
    for i in range(len(word)):
        if word[i] == c:
            blur_list[i] = c
            ...
    ...
    return blur_list


welcome()
