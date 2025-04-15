# Projekt 1: Hangman

# Skapa en version av det klassiska spelet Hangman.

# Datorn väljer ett slumpmässigt ord från en fördefinierad lista av ord.

# Spelet visar hur många bokstäver ordet består av, men inte vilka bokstäver som är rätt.

# Spelaren ska gissa en bokstav i taget, och datorn ger feedback om bokstaven finns i ordet eller inte.

# Spelet fortsätter tills spelaren har gissat hela ordet eller har gjort tillräckligt många felaktiga gissningar.

import random

words = ["johan", "eiemi", "noel"]
chosen_word = words[random.randrange(0, len(words))]

player_guess = []
guessed_letters = set()
player_points = 5

for word in chosen_word:
  player_guess += "_"

print(f"""
      Welcome to Hangman!
      The word you have choosen contains {len(chosen_word)} letters.
      Your task is to guess the word before your {player_points} points run out...
      Or if you're lucky, guess the right word!
      """)

while player_points > 0 and player_guess != list(chosen_word):
  guessed_letter = input("\nGuess a letter in the word -> ")
  
  if guessed_letter not in guessed_letters:
    guessed_letters.add(guessed_letter)
  else:
    print(f"\nYou've already guessed at {guessed_letter}!")
    continue
  
  if guessed_letter in chosen_word:
    for i in range(0, len(chosen_word)):
      if guessed_letter == chosen_word[i]:
        player_guess[i] = guessed_letter
    print(f"\nThe letter '{guessed_letter}' was in the word.")
    print(player_guess)
    
  else:
    player_points -= 1
    print(f"\nYou have {player_points} points left.")
    if player_points == 0:
      print(f"\nSorry to see you go.\nThe chosen word was '{chosen_word}'\nTry again!")