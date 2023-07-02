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
Thu 15 Jun 2023 06:30:01 PM UTC
Fri 16 Jun 2023 07:00:01 AM UTC
Sat 17 Jun 2023 07:00:01 AM UTC
Sun 18 Jun 2023 07:00:01 AM UTC
Mon 19 Jun 2023 07:00:01 AM UTC
Tue 20 Jun 2023 07:00:01 AM UTC
Wed 21 Jun 2023 07:00:01 AM UTC
Thu 22 Jun 2023 07:00:01 AM UTC
Fri 23 Jun 2023 07:00:01 AM UTC
Sat 24 Jun 2023 07:00:01 AM UTC
Sun 25 Jun 2023 07:00:01 AM UTC
Mon 26 Jun 2023 07:00:01 AM UTC
Tue 27 Jun 2023 07:00:01 AM UTC
Wed 28 Jun 2023 07:00:01 AM UTC
Thu 29 Jun 2023 07:00:01 AM UTC
Fri 30 Jun 2023 07:00:01 AM UTC
Sat 01 Jul 2023 07:00:01 AM UTC
Sun 02 Jul 2023 07:00:01 AM UTC
