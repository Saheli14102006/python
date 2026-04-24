import random
def game():
    print("Welcome to the Number Guessing Game!")
    score = random.randint(1, 100)
    # fetch the hiscore
    with open('hiscore.txt', 'r') as f:
        hiscore = f.read()
        if hiscore!='':
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f'your score:{score}')
    if (score>hiscore or hiscore==''):
        #write this hiscore to the file
        with open('hiscore.txt', 'w') as f:
            f.write(str(score))
    return score

game()