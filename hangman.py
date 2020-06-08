import random


def set_letter(cw, w, l):
    ind = 0
    while l in cw[ind:]:
        ind = cw.find(l, ind)
        w = w[:ind] + l + w[ind + 1:]
        ind = ind + 1
        if ind == len(cw):
            break
    return w


def errors (letter):
    if letter in set_guessed:
        print("You already typed this letter")
        return True
    if len(letter) != 1:
        print("You should input a single letter")
        return True
    if not letter.islower():
        print("It is not an ASCII lowercase letter")
        return True
    return False


print("H A N G M A N")

words=open("E:\words.txt","r")

word_list =[]
for word in words:
    word_list.append(word.strip())


while True:
    ch = input('Type "play" to play the game, "exit" to quit:')
    if ch != 'play':
        break

    correct_word = random.choice(word_list)
    word = len(correct_word) * "-"
    lives = 8
    set_word = set(correct_word)
    set_guessed = set()

    while lives > 0:
        print()
        print(word)

        letter = input("Input a letter:")

        if errors(letter):
            continue

        set_guessed.update(letter)

        if letter not in set_word:
            print("No such letter in the word")
            lives -= 1
            continue

        word = set_letter(correct_word, word, letter)

        if word == correct_word:
            print("You guesses the word " + correct_word + "!\nYou survived!\n")
            break
    if lives == 0:
        print("You are hanged!\nThe correct word is "+correct_word)
