# Python Hangman
Simple exploration on building a hangman game with python. Classis rules of the game apply here.
- If the user guesses a letter correctly, they will advance and not lose any of their remaining tries
- If a user guesses incorrectly, their remaining tries will decrement by 1

## Prerequisites
- Python 3.x

## Installation
Only a CLI is required to run this project:
1. ```$ cd python-hangman```
2. ```$ python main.py```

## General Notes
- The amount of tries is determined by the length of the word
- ```tries_max = word_len - (word_len / 2)```
- Once the user guesses incorrectly <n> times or guesses the word correctly, the game will end
