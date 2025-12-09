# count = 1
# while count <= 5 :
#     print("hi i am in loops", count)
#     count += 1
# print(count)

# Lets Practice

# # Print numbers from 1 to 100.
# i = 1
# while i <=100:
#     print(i)
#     i += 1

# # Print numbers from 100 to 1.
# i = 100
# while i >=1:
#     print(i)
#     i -= 1

# # Print the multiplication table of a number n.

# n = int(input("enter any , which you want to multiplication "))
# i = 1
# while i <=10:
#     print(n*i)
#     i += 1

# # Print the elements of the following list using a loop: 
# # [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# # ["ironman", "thor", "superman", "batman"]    

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]  
# heroes = ["ironman", "thor", "superman", "batman"]


# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1

# i = 0
# while i < len(heroes):
#     print(heroes[i])
#     i += 1

# Search for a number x in this tuple using loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81,100) 

# x = int(input("enter any value from tuple, which you want to find "))
# num = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
# i =0 
# while i < len(num):
#     if(num[i] == x):
#         print("found at index", i)
#     i += 1\


# import random

# # 1. Initialization
# MAX_GUESSES = 5
# secret_number = random.randint(1, 20)
# guess_count = 0
# guessed = False

# print("Welcome to the Number Guessing Game!")
# print(f"I'm thinking of a number between 1 and 20. You have {MAX_GUESSES} guesses.")

# # 2. The Main Game Loop (while loop)
# while guess_count < MAX_GUESSES and not guessed:
#     # Tell the user how many guesses they have left
#     print(f"\nGuess {guess_count + 1} of {MAX_GUESSES}:")

#     # Get user input and handle potential errors
#     try:
#         user_guess = int(input("Take a guess: "))
#         guess_count += 1
#     except ValueError:
#         print("That's not a valid number! Try again.")
#         # We don't increment the count here if the input was invalid
#         continue

#     # 3. Game Logic (Inside the loop)
#     if user_guess == secret_number:
#         guessed = True
#         break # Exit the loop immediately upon success
#     elif user_guess < secret_number:
#         print("Your guess is too low.")
#     else:
#         print("Your guess is too high.")

# # 4. Game Outcome (After the loop finishes)
# print("--- Game Over ---")

# if guessed:
#     print(f"🎉 Congratulations! You guessed the number {secret_number} in {guess_count} attempts!")
# else:
#     print(f"😔 Sorry, you ran out of guesses. The number was {secret_number}.")


# # Rock, Paper, Scissors Game

# import random

# # List of valid moves for the computer
# moves = ["rock", "paper", "scissors"]
# score_player = 0
# score_computer = 0

# print("Welcome to Rock, Paper, Scissors!")

# # The main loop keeps the game running until the player quits
# while True:
#     print("\n--- New Round ---")
    
#     # 1. Get player input
#     player_choice = input("Enter your move (rock, paper, scissors) or 'quit' to end the game: ").lower()
    
#     # Check for the exit condition (Loop control)
#     if player_choice == 'quit':
#         break # Exits the while loop
    
#     # Input validation
#     if player_choice not in moves:
#         print("Invalid move. Please choose rock, paper, or scissors.")
#         continue # Jumps to the start of the next loop iteration
        
#     # 2. Computer makes a move
#     computer_choice = random.choice(moves)
#     print(f"Computer chose: {computer_choice}")
    
#     # 3. Determine the winner (Game Logic)
    
#     # Check for a tie
#     if player_choice == computer_choice:
#         result = "It's a tie!"
    
#     # Check for player win conditions
#     elif (player_choice == "rock" and computer_choice == "scissors") or \
#          (player_choice == "paper" and computer_choice == "rock") or \
#          (player_choice == "scissors" and computer_choice == "paper"):
#         result = "You win!"
#         score_player += 1
        
#     # All other cases are a computer win
#     else:
#         result = "The computer wins!"
#         score_computer += 1
        
#     # 4. Display results
#     print(result)
#     print(f"Current Score: Player {score_player} | Computer {score_computer}")

# # 5. Final results after the loop is broken
# print("\n--- Final Results ---")
# print(f"Total Score: Player {score_player} | Computer {score_computer}")
# print("Thanks for playing!")