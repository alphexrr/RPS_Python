# RPS_Python

import random

print("==============================================")
print(" IntelliMove - AI Based Rock Paper Scissors")
print("==============================================")

# Scores
user_score = 0
computer_score = 0
draw_score = 0

# Store user move history
user_history = []

# Function to predict user's next move
def predict_user_move(history):

    if len(history) == 0:
        return random.choice(["Rock", "Paper", "Scissors"])

    # Count frequency of moves
    move_count = {
        "Rock": history.count("Rock"),
        "Paper": history.count("Paper"),
        "Scissors": history.count("Scissors")
    }

    # Predict most frequent move
    predicted_move = max(move_count, key=move_count.get)
    return predicted_move


# Function to generate computer move
def computer_move(history):

    predicted = predict_user_move(history)

    # Counter move logic
    if predicted == "Rock":
        return "Paper"

    elif predicted == "Paper":
        return "Scissors"

    elif predicted == "Scissors":
        return "Rock"

    else:
        return random.choice(["Rock", "Paper", "Scissors"])


# Function to decide winner
def decide_winner(user, computer):

    global user_score
    global computer_score
    global draw_score

    if user == computer:
        draw_score += 1
        return "Draw"

    elif (
        (user == "Rock" and computer == "Scissors") or
        (user == "Paper" and computer == "Rock") or
        (user == "Scissors" and computer == "Paper")
    ):
        user_score += 1
        return "User"

    else:
        computer_score += 1
        return "Computer"


# Main Game Loop
while True:

    print("\nChoose an option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter your choice (1/2/3): ")

    # Input Validation
    if choice == "1":
        user_choice = "Rock"

    elif choice == "2":
        user_choice = "Paper"

    elif choice == "3":
        user_choice = "Scissors"

    else:
        print("Invalid Input! Please enter 1, 2, or 3.")
        continue

    # Store user move
    user_history.append(user_choice)

    # Generate computer move
    comp_choice = computer_move(user_history[:-1])

    print("\nUser Choice :", user_choice)
    print("Computer Choice :", comp_choice)

    # Decide result
    result = decide_winner(user_choice, comp_choice)

    print("\n========== RESULT ==========")

    if result == "User":
        print("You Win!")

    elif result == "Computer":
        print("Computer Wins!")

    else:
        print("Match Draw!")

    # Show AI Prediction Info
    predicted_move = predict_user_move(user_history)

    print("\n------ AI Analysis ------")
    print("Predicted User Move :", predicted_move)

    # Scoreboard
    print("\n========== SCOREBOARD ==========")
    print("User Wins :", user_score)
    print("Computer Wins :", computer_score)
    print("Draws :", draw_score)

    # Move History
    print("\nMove History :", user_history)

    # Replay Option
    play_again = input("\nDo you want to play again? (yes/no): ")

    if play_again.lower() != "yes":
        print("\n===================================")
        print("Thank You for Playing IntelliMove!")
        print("===================================")
        break
