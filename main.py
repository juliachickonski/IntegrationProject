"""Integration Project Final"""
import random

_author_ = "Julia Chickonski"


def basic_calc():
    """Acts as a basic calculator"""
    print("\nWhat can I help you calculate today?")
    print("1. Exponents")
    print("2. Multiplication")
    print("3. Division")
    print("4. Addition")
    print("5. Subtraction")
    print("6. Even or odd number")
    while True:
        try:
            math_task = int(input())
            break
        except ValueError:
            print("\nInvalid input. Please use numbers only. ")

    if math_task == 1:
        while True:
            try:
                base_num = float(input("What number is the base? "))
                exponent = float(input("What is the power? "))
                print(base_num ** exponent)
                break
            except ValueError:
                print("\nInvalid input. Please use numbers only. ")

    elif math_task == 2:
        while True:
            try:
                multiply_1 = float(input("What is the first number? "))
                multiply_2 = float(input("Second Number? "))
                print(multiply_1 * multiply_2)
                break
            except ValueError:
                print("\nInvalid input. Please use numbers only. ")

    elif math_task == 3:
        while True:
            try:
                divide_1 = float(input("What number are you dividing? "))
                divide_2 = float(input("What are you dividing by? "))
                print(divide_1 / divide_2)
                break
            except ValueError:
                print("\nInvalid input. Please use numbers only. ")

    elif math_task == 4:
        while True:
            try:
                add_1 = float(input("What is the first number? "))
                add_2 = float(input("Second Number? "))
                add_1 += add_2
                print(add_1)
                break
            except ValueError:
                print("\nInvalid input. Please use numbers only. ")

    elif math_task == 5:
        while True:
            try:
                sub_1 = float(input("What is the first number? "))
                sub_2 = float(input("Second Number? "))
                print(sub_1 - sub_2)
                break
            except ValueError:
                print("\nInvalid input. Please use numbers only. ")

    elif math_task == 6:
        while True:
            try:
                number = float(input("Enter any number: "))
                if number % 2 == 0:
                    print("Even")
                else:
                    print("Odd")
                break
            except ValueError:
                print("\nInvalid input. Please use numbers only. ")
    else:
        print()


# MadLibs
# Free story from https://www.madtakes.com/libs/021.html
def mad_libs():
    """Prompts user to type out words to fill in the story"""
    print("\nTell your own story.")
    print(
        "This is a MadLibs style story where you will input nouns, verbs, "
        "etc. to fill in the story.")
    adj_1 = input("Give me an ADJECTIVE: ")
    name_1 = input("Give me a NAME: ")
    job_type = input("Give me a PROFESSION: ")
    verb_ing = input("Give me a VERB ending in -ING: ")
    plant_type = input("Give me a type of PLANT (plural): ")
    adj_2 = input("Give me an ADJECTIVE: ")
    noun_1 = input("Give me a NOUN (plural): ")
    noun_2 = input("Give me a PLURAL NOUN: ")
    name_2 = input("Give me a NAME: ")
    print(adj_1, name_1,
          'Brothers is a popular video game where you control a/an ' +
          job_type)
    print(
        'as he/she runs through levels ' + verb_ing + ' on enemies and eating '
        + plant_type)
    print(
        'to get ' + adj_2 + ' Fireflowers so that he/she can throw ' + noun_1 +
        ' at enemies.')
    print(
        'He does all this to save the ' + noun_2 + ' Kingdom from the evil ' +
        name_2 + '.')


def random_machine():
    """Decision Maker"""
    print(
        "To help you choose, I can: \n1. Roll a dice \n2. I can flip a coin. "
        "\n3. Magic 8 Ball",
        sep="")
    while True:
        try:
            choice = int(input())
            break
        except ValueError:
            print("\nInvalid input. Please use numbers only. ")
    if choice == 1:
        while True:
            try:
                sides = int(input("How many sides does the dice have? "))
                print("Your roll is: ", end=" ")
                print(random.randint(1, sides))
                break
            except ValueError:
                print("\nInvalid input. Please use numbers only. ")
    elif choice == 2:
        input("\nHeads or tails? (press any key to continue) ")
        flip = random.randint(1, 2)
        if flip == 1:
            print("Heads")
        else:
            print("Tails")
    elif choice == 3:
        input("Ask me a question (press enter)")
        shake = random.randint(1, 5)
        if shake == 1:
            print("It is Certain")
        elif shake == 2:
            print("Most likely")
        elif shake == 3:
            print("Don't Count on It")
        elif shake == 4:
            print("My sources say NO")
        elif shake == 5:
            print("Cannot predict now, come back later")
    else:
        print()


def main():
    """Main Function interface"""
    do_again = "YES" and "yes"
    while do_again == "yes":
        print("Hello! Welcome to my Integration Project")
        print("This is what I can do:", sep='')
        print("1. Calculator", sep='')
        print("2. MadLibs", sep='')
        print("3. Decision maker", sep='')
        print("4. End program")
        while True:
            try:
                task = int(input("What task would you like me to "
                                 "perform? "))
                break
            except ValueError:
                print("Invalid input. Please only use numbers 1-4.")
        if task == 1:
            basic_calc()
        elif task == 2:
            mad_libs()
        elif task == 3:
            random_machine()
        elif task == 4:
            print("Program will end now. Glad to be of help :)")
            exit()
        else:
            print()
        do_again = input("Type YES if you would like to return to the "
                         "menu. Press any other key to quit. ")
    else:
        print()


main()
