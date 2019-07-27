# Hangman project
# @Language: Python
# @Author: Stephen

word = "testerman"
word_len = len(word)
tries_max = word_len - (word_len / 2)
tries = 0
playing = True

print("Lets play Hangman!")
print("_" * word_len)
print("Tries left: " + str(tries_max - tries))

# While user hasn't reached max tries
while playing:
  guess = raw_input("Guess a letter: ")

  if guess in word:
    print("Correct!")
  else:
    print("Sorry not found")
    tries += 1

    # End game if max tries is reached
    if tries == tries_max:
      print("GAME OVER")
      playing = False
