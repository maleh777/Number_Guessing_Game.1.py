import random
 
def number_guessing_game(game_mode="singleplayer"):
    """
    plays a number guessing game with various options.
      -Singleplayer
      -Multiplayer
      -AI oponent
    Args:
      game_mode: The game mode to play("singleplayer", "multiplayer", "ai").
                 Defaults to "singleplayer".
   
    """
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    hint_count = 0
    attempts = 0

    
    if game_mode == "singleplayer": 
      lower_bound = 1
      upper_bound = 100
      secret_number = random.randint(lower_bound, upper_bound)
      hint_count = 0
      attempts = 0   
      while True:
         try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < secret_number:
               print("Too low!")
            elif guess > secret_number:
               print("Too high!")
            else:
               print(f"congratulations! You guessed the numberin {attempts} attempts")
               break

            # Hint logic
            if attempts % 3 == 0 and hint_count < 1:
                  hint_count += 1
                  hint = random.choice(["The number is even.", "The number is odd", 
                                      "The number is divisible by 3",
                                      "The number is greater than 50."])
                  print(f"Hint: {hint}")            

         except ValueError:
            print("invalid input.please enter a number.")

    elif game_mode == "multiplayer":
      lower_bound = 1
      upper_bound = 100
      secret_number = random.randint(lower_bound, upper_bound)
      current_player = "player 1" 
      player1_score = 0
      player2_score = 0
      hint_count = 0 
      attempts = 0 

      while True:
         print(f"it's{current_player}'s turn")
         try:
             guess = int(input("Take a guess: "))
             attempts += 1 

             if guess < secret_number:
               print("Too low!")
             elif guess > secret_number:
               print("Too high!")
             else:
                  print(f"congratulations, {current_player}! You guessed the numberin {attempts} attempts")
                  if current_player == "player 1":
                     player1_score = attempts
                  else:
                      player2_score = attempts      
                  break

             # Hint logic
             if attempts % 3 == 0 and hint_count < 1:
                  hint_count += 1
                  hint = random.choice(["The number is even.", "The number is odd", 
                                      "The number is divisible by 3",
                                      "The number is greater than 50."])
                  print(f"Hint: {hint}")

             # switch players
             if current_player == "player 1":
                current_player = "player 2"
             else:
                current_player = "player 1"
           
         except ValueError:
          print("invalid input.please enter a number.")               

             # Display scores
          print(f"\nplayer 1 score: {player1_score}")
          print(f"\nplayer 2 score: {player2_score}")

         if player1_score < player2_score:
            print("\nplayer 1 wins!")
         elif player2_score < player1_score:
           print("\nplayer 2 wins!")
         else:
              print("\nIt's a tie!")

    elif game_mode == "ai":
         lower_bound = 1
         upper_bound = 100
         secret_number = random.randint(lower_bound, upper_bound)
         ai_attempts = 0
         ai_guess = 0

         while ai_guess != secret_number:
            ai_guess = random.randint(lower_bound, upper_bound)                    
            ai_attempts += 1

         if ai_guess < secret_number:
               print(f"AI guessed {ai_guess}. Too low!")
               lower_bound = ai_guess + 1
         elif  ai_guess < secret_number:
               print(f"AI guessed {ai_guess}. Too High!")
               upper_bound = ai_guess - 1
         else:
               print(f"AI guessed the number in {ai_attempts} attempts!")      

if __name__ == "__main__":
    game_mode = input("choose game mode: (singleplayer, multipleplayer, ai) ") 
    number_guessing_game(game_mode)

      