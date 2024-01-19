import random
while True:
    valid_qtds = None
    qtds = 0

    qtd = (input('Enter here how many dices you want to roll: '))

    try: # Check if it's a int number.
        qtds = int(qtd)
        if qtds > 0:
            valid_qtds = True
        else:
            print('Please insert a number higher than 0.')
            continue
    except:
        if valid_qtds is None:
            print('Invalid. ')
            continue

    side = input('''
    [1] d4 \n
    [2] d6 \n
    [3] d8 \n
    [4] d12 \n
    [5] d20 \n
    [6] d100 \n
Choose the dice type: ''') 

    valid_side = None

    try: # Check if it's a int number.
        sides = int(side)
        if sides <= 6 and sides >=1:
            valid_side = True
        else:
            print('Please insert a number between 1 and 6.')
            continue
    except ValueError:
        if valid_side is None:
            print('Invalid. ') 
            continue

    res = 0
    somado = 0
    rolled = 0

    while rolled < qtds:
        if sides == 1:
            res = random.randint(1, 4)
        elif sides == 2:
            res = random.randint(1, 6)
        elif sides == 3:
            res = random.randint(1, 8)
        elif sides == 4:
            res = random.randint(1, 12)
        elif sides == 5:
            res = random.randint(1, 20)
        elif sides == 6:
            res = random.randint(1, 100)

        rolled += 1
        somado += res
        
        print(f'{rolled} {res}')
    if qtds > 1: 
        soma = input('Sum the results? [n]o [y]es: ').lower().startswith('y')
        if soma:
            print(f'Total: {somado}.')

    sair = input('Continue? [n]o / [y]es: ').lower().startswith('n')
        
    if sair:
        break
            

