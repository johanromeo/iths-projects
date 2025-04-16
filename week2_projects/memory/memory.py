# Projekt 2: Memory

# Skapa en version av spelet Memory.

# Datorn väljer ett antal slumpmässiga siffror eller bokstäver (beroende på svårighetsgrad) och visar dem i en viss ordning.

# Sedan visar datorn samma siffror eller bokstäver igen, men denna gång blandat.

# Spelaren ska gissa i vilken ordning siffrorna eller bokstäverna visades första gången.

# Spelet fortsätter tills spelaren har gissat rätt ordning.

import random
import os
import time

# Lists to hold the numbers
original_nums = []
shuffled_nums = []

# Add random 5 random integers, 0 - 5, to the original_nums list
for i in range(5):
  random_number = random.randint(0,5)
  original_nums.append(random_number)
  

# Show user the original_nums list to memorize
for num in original_nums:
  print(num, end=", ")
  
# Ask player to memorize before clearing the screen to avoid cheating
print("\nYou have 5 seconds to memorize the order of the numbers.")
time.sleep(5)
os.system("cls||clear")

# Confuse player by showing the shuffled_nums
print("Here are the numbers again... but shuffled. Just to confuse you!")
shuffled_nums = original_nums.copy()
random.shuffle(shuffled_nums)

for num in shuffled_nums:
  print(num, end=", ")
  
  
# Now it's showtime baby! Ask the player to guess which number came at what index in original_nums list
print("Your task is pretty straight forward - enter the order of which the first numbers appeared!\n")
      
# The first index in original_nums list
index_count = 0

# Game loops until player guesses the correct order of nums in original_nums list
while index_count < len(original_nums):
  player_guess = int(input(f"Which number appeared on index '{index_count}'?"))
  if player_guess == original_nums[index_count]:
    print("Good job!")
    index_count += 1
  else:
    print("Hmmm... That was not right at all!\n")
