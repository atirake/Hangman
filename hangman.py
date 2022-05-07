import random
import string


def output(display):
    print("".join(display))


print('H A N G M A N  # 8 attempts')
won = 0
lost = 0
while True:
    begin = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if begin == 'play':
        print()
        words = ['python', 'java', 'swift', 'javascript']
        word = []
        letters = []
        choice = random.choice(words)
        for letter in choice:
            print('-', end='')
            word.append('-')
        print()
        attempts = 8
        game = False
        while attempts > 0:
            letter = input('Input a letter: ')
            if len(letter) != 1:
                print('Please, input a single letter.')
                output(word)
                continue
            elif letter not in list(string.ascii_lowercase):
                print('Please, enter a lowercase letter from the English alphabet.')
                output(word)
                continue
            elif letter in letters:
                print("You've already guessed this letter.")
                output(word)
                continue
            else:
                letters.append(letter)
                if letter in choice:
                    for index, alpha in enumerate(choice):
                        if alpha == letter:
                            if word[index] != letter:
                                word[index] = letter
                else:
                    print("That letter doesn't appear in the word.")
                    attempts -= 1
                output(word)
                if ("".join(word)) == choice:
                    print(f'You guessed the word {choice}!')
                    game = True
                    break
                print()
        if game:
            won += 1
        else:
            lost += 1
        print('You survived!' if game else 'You lost!')
    elif begin == 'results':
        print(f'You won: {won} times.')
        print(f'You lost: {lost} times.')
        continue
    elif begin == 'exit':
        break
    else:
        continue
