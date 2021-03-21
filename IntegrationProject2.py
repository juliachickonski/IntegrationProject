#Julia Chickonksi
# My integration project
#Basic Calculator

def basic_calc():
    print("\nWhat can I help you calculate today?")
    print("1. Exponents")
    print("2. Multiplication")
    print("3. Divison")
    print("4. Addition")
    print("5. Subtraction")
    print("6. Even or odd number")
    math_task = int(input())

    if math_task == 1:
        base_num = float(input("What number is the base? "))
        exponent = float(input("What is the power? "))
        print(base_num ** exponent)

    elif math_task == 2:
        mult_1 = float(input("What is the first number? "))
        mult_2 = float(input("Second Number? "))
        print(mult_1 * mult_2)

    elif math_task == 3:
        divide_1 = float(input("What number are you dividing? "))
        divide_2 = float(input("What are you dividing by? "))
        print(divide_1 / divide_2)

    elif math_task == 4:
        add_1 = float(input("What is the first number? "))
        add_2 = float(input("Second Number? "))
        print(add_1 + add_2)

    elif math_task == 5:
        sub_1 = float(input("What is the first number? "))
        sub_2 = float(input("Second Number? "))
        print(sub_1 - sub_2)

    elif math_task == 6:
        number = float(input("Enter any number: "))
        if (number % 2 == 0):
            print("Even")
        else:
            print("Odd")
    else:
        print()

#MadLibs
# Prompts user to type out words to fill in the story
# Free story from https://www.madtakes.com/libs/021.html
def mad_libs():
    print("\nTell your own story.")
    print("This is a MadLibs style story where you will input nouns, verbs, etc. to fill in the story.")
    adj_1 = input("Give me an ADJECTIVE: ")
    name_1 = input("Give me a NAME: ")
    job_type = input("Give me a PROFESSION: ")
    verb_ing = input("Give me a VERB ending in -ING: ")
    plant_type = input("Give me a type of PLANT (plural): ")
    adj_2 = input("Give me an ADJECTIVE: ")
    noun_1 = input("Give me a NOUN (plural): ")
    noun_2 = input("Give me a PLURAL NOUN: ")
    name_2 = input("Give me a NAME: ")

    print(adj_1, name_1, 'Brothers is a popular videogame where you control a/an ' + job_type)
    print('as he/she runs through levels ' + verb_ing + ' on enemies and eating ' + plant_type)
    print('to get ' + adj_2 + ' fireflowers so that he/she can throw ' + noun_1 + ' at enemies.')
    print('He does all this to save the ' + noun_2 + ' Kingdom from the evil ' + name_2 + '.')


# Decision Maker
import random
def random_machine():
    print("To help you choose, I can: \n1. Roll a dice \n2. I can flip a coin. \n3. Magic 8 Ball", sep="")
    choice = int(input())
    if choice == 1:
        sides = int(input("How many sides does the dice have?"))
        print("Your roll is: ", end=" ")
        print(random.randint(1,sides))
    elif choice == 2:
        flip = random.randint(1,2)
        if flip == 1:
            print("Heads")
        else:
            print("Tails", sep=" ")
    elif choice == 3:
        x = input("Ask me a question (press enter)")
        shake = random.randint(1,5)
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
        print(sep=" ")


def main():
    do_again = "yes"
    print("This is what I can do:", sep='')
    print("1. Basic Calculations", sep='')
    print("2. MadLibs", sep='')
    print("3. Decision maker", sep='')
    print("4. End program")
    while do_again == "yes":
        task = int(input("What would you like to do? "))
        if task == 1:
            basic_calc()
        elif task == 2:
            mad_libs()
        elif task == 3:
            random_machine()
        else:
            print("Program will end now")
        do_again = input("If you want me to perform another task, type 'yes'. \nType anythinge else to quit." )
main()