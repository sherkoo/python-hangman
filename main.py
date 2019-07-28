# Hangman project
# @Language: Python
# @Author: Stephen

import random

word_list = ["disturbed", "korn", "limpbizkit", "slipknot", "deftones", "metallica"]
word_rnd = random.randint(0, len(word_list) - 1)
word = word_list[word_rnd]
word_len = len(word)
word_guess = []

for x in range(word_len):
    word_guess.append("_")

tries_max = word_len - (word_len / 2) + 3

# Init
tries = 0
playing = True

# Start the game
print("Lets play Hangman!")
print(word_guess)

# split the word into individual chars
def split(word):
    return [char for char in word]

# While user hasn't reached max tries
while playing:
  guess = raw_input("Guess a letter: ").lower()

  if guess in word:
    # User guesses a correct letter
    print("=============================")
    print("Letter Found!")
    found = [pos for pos, char in enumerate(word) if char == guess]
    # insert letter X found times
    for f in found:
        word_guess[f] = guess

    print(word_guess)
    print("Tries left: " + str(tries_max - tries))

    # end game if all letters are guessed
    if word_guess == split(word):
        print("YOU WIN!")
        playing = False

  else:
    print("Sorry not found")
    tries += 1
    print("Tries left: " + str(tries_max - tries))

    # End game if max tries is reached
    if tries == tries_max:
      print("GAME OVER")
      playing = False
