def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("Guess the Animal")
guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")
guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "Cheetah")
guess3 = input("Which is the larget animal? ")
check_guess(guess3, "Blue Whale")
print("Your Score is "+ str(score))


Mon 12 Jun 2023 09:39:08 PM CST
Mon 12 Jun 2023 09:39:44 PM CST
Tue 13 Jun 2023 09:58:03 PM UTC
Thu 15 Jun 2023 04:23:19 PM UTC
Thu 15 Jun 2023 04:24:00 PM UTC
Thu 15 Jun 2023 05:49:30 PM UTC
Thu 15 Jun 2023 05:50:01 PM UTC
Thu 15 Jun 2023 06:00:01 PM UTC
Thu 15 Jun 2023 06:10:01 PM UTC
Thu 15 Jun 2023 06:20:01 PM UTC
