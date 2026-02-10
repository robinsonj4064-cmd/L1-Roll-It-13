[C_01_yes_no_basic.py](https://github.com/user-attachments/files/25222170/C_01_yes_no_basic.py)


while True:
    want_instructions = input("Do you want to see the instructions").lower()

    #check the user say yes / no
    if want_instructions == "yes" or want_instructions == "y":
        print("you said yes")
        break
    elif want_instructions == "no" or want_instructions == "n":
        print("you said no")
        break
    else:
        print("please enter yes / no")
        continue

print("we done")
