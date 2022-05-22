import random


def rand():
    randNo = random.randint(1, 3)
    if randNo == 1:
        comp = 's'
    elif randNo == 2:
        comp = 'w'
    elif randNo == 3:
        comp = 'g'
    return comp


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


def help():
    print('For your information\nSnake beats Water\nWater beats Gun\nGun beats Snake')


def func(count_comp, count_you):
    print(f'\nEXIT')
    print(f'Computer score is: {count_comp}')
    print(f'Your score is: {count_you}')
    print('*'*30, 'Thanks for playing', '*'*30)
