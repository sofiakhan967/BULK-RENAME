import random

roll_dice= "yes"
def dice():
    while roll_dice=='yes':
        user= (input(" Do you want to play? Yes or No : "))
        if user == "no":
            print("Thanks , You can start again to play .  ")
            break
        else:

            print(" dice is rolling .......")
            print("rolling ...... rolling.......")
            diceroll=random.randint(1,6)
            print('Dice value is : ', diceroll)
dice()


