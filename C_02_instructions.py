#functions go here

def yes_no(question):
    """Checks user response to a question is yes / no (y/n), return 'yes' or 'no'"""

    while True:

        response = input(question).lower()

        #check the user say yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Shows user instructions"""

    print("Roll the dice to gamble ur life away")


#Main routine

# ask the user if they want intructions (check they said yes / no)
want_instructions = yes_no("Do you want to see the instructions").lower()

# Display the intructions if the user want to see them...
if want_instructions == "yes":
    instructions()

print()
print("Program continues")
