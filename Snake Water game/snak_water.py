import comp

count_comp = 0
count_you = 0
n = input('Enter (1)To play, (2)To exit and (3)For help: ')
if n == '1':
    while True:
        print('Comp Turn: Snake(s) Water(w) or Gun(g)')
        you = input(
            'Your Turn: Snake(s), Water(w) or Gun(g)?[Press 2 to quit anytime] ')
        you = you.lower()
        if you == '2':
            comp.func(count_comp, count_you)
            break
        elif you == 's' or you == 'w' or you == 'g':
            com = comp.rand()
            a = comp.gameWin(com, you)
            print(f'Computer chose {com}')
            print(f'You chose {you}')
            if a == None:
                print('The game is tie')
            elif a:
                print('You win!')
                count_you += 1
            else:
                print('You lose!')
                count_comp += 1
        else:
            print('Choose only Snake(s) or Water(w) or Gun(g)')
elif n == '2':
    comp.func(count_comp, count_you)
elif n == '3':
    comp.help()
else:
    print('Please enter either 1 or 2 or 3')
    print('*'*30, 'Thanks for playing', '*'*30)
