import time

def play_bollywood_game():
    print(" Welcome to the Bollywood Trivia Game! ")
    print("------------------------------------------")
    
    # 1. LIST for Questions
    questions_list = [
        "Which movie features the famous dialogue 'Kitne aadmi the'?",
        "Who played the role of Rancho in the movie '3 Idiots'?",
        "Complete the movie title: Kabhi Khushi Kabhie ______?",
        "Which movie is about a wrestler father training his daughters to win gold?",
        "Who is known as the 'King Khan' of Bollywood?"
    ]

    # 2. DICTIONARY for Answers
    # The keys match the questions in the list, and values are the answers
    answers_dict = {
        "Which movie features the famous dialogue 'Kitne aadmi the'?": "Sholay",
        "Who played the role of Rancho in the movie '3 Idiots'?": "Aamir Khan",
        "Complete the movie title: Kabhi Khushi Kabhie ______?": "Gham",
        "Which movie is about a wrestler father training his daughters to win gold?": "Dangal",
        "Who is known as the 'King Khan' of Bollywood?": "Shah Rukh Khan"
    }

    score = 0

    # Loop through the list of questions
    for question in questions_list:
        print(f"\n Question: {question}")
        
        # Get user input
        user_answer = input("Your Answer: ").strip()

        # Get the correct answer from the dictionary using the question as the key
        correct_answer = answers_dict[question]

        # Check if the answer is correct (ignoring capitalization)
        if user_answer.lower() == correct_answer.lower():
            print(" Correct! You won this round.")
            score += 1
        else:
            print(f" Wrong! The correct answer was: {correct_answer}")
            print("Try again next time!")

        time.sleep(0.5) # Short pause for better experience

    # Final Score
    print("\n------------------------------------------")
    print(f"Game Over! Your final score is: {score}/{len(questions_list)}")
    if score == len(questions_list):
        print(" Super Hit! You are a true Bollywood fan!")
    elif score >= 3:
        print(" Hit! Good job.")
    else:
        print(" Flop! Better luck next time.")

if __name__ == "__main__":
    play_bollywood_game()