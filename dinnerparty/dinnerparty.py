import random


dictionary = {}
count = 0


def create_party():
    welcome_msg = "Enter the number of friends joining (including you):\n> "
    enter_nms = "Enter the name of every friend (including you), each on a new line:\n> "
    no_one = "No one is joining for the party"
    global count

    count = int(input(welcome_msg))
    if count <= 0:
        print(no_one)
        return

    for i in range(count):
        name = input(enter_nms)
        dictionary[name] = 0
        ...
    total_amount()
    ...


def total_amount():
    ent_am = "Enter the total amount:\n> "

    total = int(input(ent_am))
    bill = format_bill(total/count)
    for i in dictionary:
        dictionary[i] = bill
        ...
    get_lucky(bill)
    ...


def get_lucky(bill):
    q_lucky = "Who is lucky? feature? Write Yes/No:\n> "
    lucky_one = "{0} is the lucky one!"

    ans = input(q_lucky).strip().lower()

    if ans == "yes":
        lucky = get_randkey(dictionary)
        global count
        new_count = count-1 if count > 1 else 1
        dictionary[lucky] = 0

        for i in dictionary:
            if i != lucky:
                dictionary[i] = format_bill(dictionary[i]+bill/new_count)
            ...
        print(lucky_one.format(lucky))
        ...
    print(dictionary)
    ...


def format_bill(bill):
    bill = float(bill)
    return int(bill) if bill.is_integer() else float('%.2f' % bill)


def get_randkey(d: dict):
    return random.choice(list(d.keys()))


create_party()
