import random


def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True

    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


count = 0
countcomp = 0
while(True):
    print("Comp turn: Snake(s) Water(w) or Gun(g)? Computer has decided.")
    rand = random.randint(1, 3)
    if rand == 1:
        comp = 's'
    elif rand == 2:
        comp = 'w'
    elif rand == 3:
        comp = 'g'
    you = input("Your turn: Snake(s) Water(w) or Gun(g)? Press 0 to exit. ")
    if you == '0':
        break
    a = gameWin(comp, you)
    print(f"Computer chose {comp}")
    print(f"You chose {you}")
    if a == None:
        print("Game is a tie")
    elif a:
        print("You win")
        count += 1
    else:
        print("You lose")
        countcomp += 1
    print(f"Score: You:{count} Computer:{countcomp}")
