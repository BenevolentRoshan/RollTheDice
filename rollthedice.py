# Rolling th dice untill 6 arrives

import random
def check6(x):
    if x=="Y":
        dice=random.choice([1,2,3,4,5,6])
        user=0
        while dice!=6:
            user=input(f"You got {dice}. Do you want to try again e.g Y/N: ").capitalize()
            if user=="Y":
                return check6(user)
            else:
                return "Thank you for Playing"
        return "Yay you got 6"
    else:
        return "Thank you for playing"

x=input("Do you want to roll the dice: Y/N: ").capitalize()
print(check6(x))