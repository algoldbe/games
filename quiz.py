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
Mon 03 Jul 2023 07:00:01 AM UTC
Tue 04 Jul 2023 07:00:01 AM UTC
Wed 05 Jul 2023 07:00:01 AM UTC
Thu 06 Jul 2023 07:00:01 AM UTC
Fri 07 Jul 2023 07:00:01 AM UTC
Sat 08 Jul 2023 07:00:01 AM UTC
Sun 09 Jul 2023 07:00:01 AM UTC
Mon 10 Jul 2023 07:00:01 AM UTC
Tue 11 Jul 2023 07:00:01 AM UTC
Wed 12 Jul 2023 07:00:01 AM UTC
Thu 13 Jul 2023 07:00:01 AM UTC
Fri 14 Jul 2023 07:00:01 AM UTC
Sat 15 Jul 2023 07:00:01 AM UTC
Sun 16 Jul 2023 07:00:01 AM UTC
Mon 17 Jul 2023 07:00:01 AM UTC
Tue 18 Jul 2023 07:00:01 AM UTC
Wed 19 Jul 2023 07:00:01 AM UTC
Thu 20 Jul 2023 07:00:01 AM UTC
Fri 21 Jul 2023 07:00:01 AM UTC
Sat 22 Jul 2023 07:00:01 AM UTC
Sun 23 Jul 2023 07:00:01 AM UTC
Mon 24 Jul 2023 07:00:01 AM UTC
Tue 25 Jul 2023 07:00:01 AM UTC
Wed 26 Jul 2023 07:00:01 AM UTC
Thu 27 Jul 2023 07:00:01 AM UTC
Fri 28 Jul 2023 07:00:01 AM UTC
Sat 29 Jul 2023 07:00:01 AM UTC
Sun 30 Jul 2023 07:00:01 AM UTC
Mon 31 Jul 2023 07:00:01 AM UTC
Tue 01 Aug 2023 07:00:01 AM UTC
Wed 02 Aug 2023 07:00:01 AM UTC
Thu 03 Aug 2023 07:00:01 AM UTC
Fri 04 Aug 2023 07:00:01 AM UTC
Sat 05 Aug 2023 07:00:01 AM UTC
Sun 06 Aug 2023 07:00:01 AM UTC
Mon 07 Aug 2023 07:00:01 AM UTC
Tue 08 Aug 2023 07:00:01 AM UTC
Wed 09 Aug 2023 07:00:01 AM UTC
Thu 10 Aug 2023 07:00:01 AM UTC
Fri 11 Aug 2023 07:00:01 AM UTC
Sat 12 Aug 2023 07:00:01 AM UTC
Sun 13 Aug 2023 07:00:01 AM UTC
Mon 14 Aug 2023 07:00:01 AM UTC
Tue 15 Aug 2023 07:00:01 AM UTC
Wed 16 Aug 2023 07:00:01 AM UTC
Thu 17 Aug 2023 07:00:01 AM UTC
Fri 18 Aug 2023 07:00:01 AM UTC
Sat 19 Aug 2023 07:00:01 AM UTC
Sun 20 Aug 2023 07:00:01 AM UTC
Mon 21 Aug 2023 07:00:01 AM UTC
Tue 22 Aug 2023 07:00:01 AM UTC
Wed 23 Aug 2023 07:00:01 AM UTC
Thu 24 Aug 2023 07:00:01 AM UTC
Fri 25 Aug 2023 07:00:01 AM UTC
Sat 26 Aug 2023 07:00:01 AM UTC
Sun 27 Aug 2023 07:00:01 AM UTC
Mon 28 Aug 2023 07:00:01 AM UTC
Tue 29 Aug 2023 07:00:01 AM UTC
Wed 30 Aug 2023 07:00:01 AM UTC
Thu 31 Aug 2023 07:00:01 AM UTC
Fri 01 Sep 2023 07:00:01 AM UTC
Sat 02 Sep 2023 07:00:01 AM UTC
Test 1
Fri Nov 24 19:48:35 UTC 2023
Fri Nov 24 19:54:56 UTC 2023
Fri Nov 24 19:55:16 UTC 2023
Fri Nov 24 19:56:44 UTC 2023
Fri Nov 24 19:57:26 UTC 2023
Fri Nov 24 19:59:02 UTC 2023
Fri Nov 24 21:11:30 UTC 2023
Sat Nov 25 07:00:01 UTC 2023
Sun Nov 26 07:00:01 UTC 2023
Mon Nov 27 07:00:01 UTC 2023
Tue Nov 28 07:00:01 UTC 2023
Wed Nov 29 07:00:01 UTC 2023
Thu Nov 30 07:00:01 UTC 2023
Fri Dec  1 07:00:01 UTC 2023
Sat Dec  2 07:00:01 UTC 2023
Sun Dec  3 07:00:01 UTC 2023
Mon Dec  4 07:00:01 UTC 2023
Tue Dec  5 07:00:01 UTC 2023
Wed Dec  6 07:00:01 UTC 2023
Thu Dec  7 07:00:01 UTC 2023
Fri Dec  8 07:00:01 UTC 2023
Sat Dec  9 07:00:01 UTC 2023
Sun Dec 10 07:00:01 UTC 2023
Mon Dec 11 07:00:01 UTC 2023
Tue Dec 12 07:00:01 UTC 2023
Wed Dec 13 07:00:01 UTC 2023
Thu Dec 14 07:00:01 UTC 2023
Fri Dec 15 07:00:01 UTC 2023
Sat Dec 16 07:00:01 UTC 2023
Sun Dec 17 07:00:01 UTC 2023
Mon Dec 18 07:00:01 UTC 2023
Tue Dec 19 07:00:01 UTC 2023
Wed Dec 20 07:00:01 UTC 2023
Thu Dec 21 07:00:01 UTC 2023
Fri Dec 22 07:00:01 UTC 2023
Sat Dec 23 07:00:01 UTC 2023
Sun Dec 24 07:00:01 UTC 2023
Mon Dec 25 07:00:01 UTC 2023
Tue Dec 26 07:00:01 UTC 2023
Wed Dec 27 07:00:01 UTC 2023
Thu Dec 28 07:00:01 UTC 2023
Fri Dec 29 07:00:01 UTC 2023
Sat Dec 30 07:00:01 UTC 2023
Sun Dec 31 07:00:01 UTC 2023
Mon Jan  1 07:00:01 UTC 2024
Tue Jan  2 07:00:01 UTC 2024
Wed Jan  3 07:00:01 UTC 2024
Thu Jan  4 07:00:01 UTC 2024
Fri Jan  5 07:00:01 UTC 2024
Sat Jan  6 07:00:01 UTC 2024
Sun Jan  7 07:00:01 UTC 2024
Mon Jan  8 07:00:01 UTC 2024
Tue Jan  9 07:00:01 UTC 2024
Wed Jan 10 07:00:01 UTC 2024
Thu Jan 11 07:00:01 UTC 2024
Fri Jan 12 07:00:01 UTC 2024
Sat Jan 13 07:00:01 UTC 2024
Sun Jan 14 07:00:01 UTC 2024
Mon Jan 15 07:00:01 UTC 2024
Tue Jan 16 07:00:01 UTC 2024
Wed Jan 17 07:00:01 UTC 2024
Thu Jan 18 07:00:01 UTC 2024
Fri Jan 19 07:00:01 UTC 2024
Sat Jan 20 07:00:01 UTC 2024
Sun Jan 21 07:00:01 UTC 2024
Mon Jan 22 07:00:01 UTC 2024
Tue Jan 23 07:00:01 UTC 2024
Wed Jan 24 07:00:01 UTC 2024
Thu Jan 25 07:00:01 UTC 2024
Fri Jan 26 07:00:01 UTC 2024
Sat Jan 27 07:00:02 UTC 2024
Sun Jan 28 07:00:01 UTC 2024
Mon Jan 29 07:00:01 UTC 2024
Tue Jan 30 07:00:01 UTC 2024
Wed Jan 31 07:00:01 UTC 2024
Thu Feb  1 07:00:01 UTC 2024
Fri Feb  2 07:00:01 UTC 2024
Sat Feb  3 07:00:01 UTC 2024
Sun Feb  4 07:00:01 UTC 2024
Mon Feb  5 07:00:01 UTC 2024
Tue Feb  6 07:00:01 UTC 2024
Wed Feb  7 07:00:01 UTC 2024
Thu Feb  8 07:00:01 UTC 2024
Fri Feb  9 07:00:01 UTC 2024
Sat Feb 10 07:00:01 UTC 2024
Sun Feb 11 07:00:01 UTC 2024
Mon Feb 12 07:00:01 UTC 2024
Tue Feb 13 07:00:01 UTC 2024
Wed Feb 14 07:00:01 UTC 2024
Thu Feb 15 07:00:01 UTC 2024
Fri Feb 16 07:00:01 UTC 2024
Sat Feb 17 07:00:01 UTC 2024
Sun Feb 18 07:00:01 UTC 2024
Mon Feb 19 07:00:01 UTC 2024
Tue Feb 20 07:00:01 UTC 2024
Wed Feb 21 07:00:01 UTC 2024
Thu Feb 22 07:00:01 UTC 2024
Fri Feb 23 07:00:01 UTC 2024
Sat Feb 24 07:00:01 UTC 2024
Sun Feb 25 07:00:01 UTC 2024
Mon Feb 26 07:00:01 UTC 2024
Tue Feb 27 07:00:01 UTC 2024
Wed Feb 28 07:00:01 UTC 2024
Thu Feb 29 07:00:01 UTC 2024
Fri Mar  1 07:00:01 UTC 2024
Sat Mar  2 07:00:01 UTC 2024
Sun Mar  3 07:00:01 UTC 2024
Mon Mar  4 07:00:01 UTC 2024
Tue Mar  5 07:00:01 UTC 2024
Wed Mar  6 07:00:01 UTC 2024
Thu Mar  7 07:00:01 UTC 2024
Fri Mar  8 07:00:01 UTC 2024
Sat Mar  9 07:00:01 UTC 2024
Sun Mar 10 07:00:01 UTC 2024
Mon Mar 11 07:00:01 UTC 2024
Tue Mar 12 07:00:01 UTC 2024
Wed Mar 13 07:00:01 UTC 2024
Thu Mar 14 07:00:01 UTC 2024
Fri Mar 15 07:00:01 UTC 2024
Sat Mar 16 07:00:01 UTC 2024
Sun Mar 17 07:00:01 UTC 2024
Mon Mar 18 07:00:01 UTC 2024
Tue Mar 19 07:00:01 UTC 2024
Wed Mar 20 07:00:01 UTC 2024
Sat Mar 23 07:00:01 UTC 2024
Sun Mar 24 07:00:01 UTC 2024
Mon Mar 25 07:00:01 UTC 2024
Tue Mar 26 07:00:01 UTC 2024
Wed Mar 27 07:00:01 UTC 2024
Thu Mar 28 07:00:01 UTC 2024
Fri Mar 29 07:00:01 UTC 2024
Sat Mar 30 07:00:01 UTC 2024
Sun Mar 31 07:00:01 UTC 2024
Mon Apr  1 07:00:01 UTC 2024
Tue Apr  2 07:00:01 UTC 2024
Wed Apr  3 07:00:01 UTC 2024
Thu Apr  4 07:00:01 UTC 2024
Fri Apr  5 07:00:01 UTC 2024
Sat Apr  6 07:00:01 UTC 2024
Sun Apr  7 07:00:01 UTC 2024
Mon Apr  8 07:00:01 UTC 2024
Tue Apr  9 07:00:01 UTC 2024
Wed Apr 10 07:00:01 UTC 2024
Thu Apr 11 07:00:01 UTC 2024
Fri Apr 12 07:00:01 UTC 2024
Sat Apr 13 07:00:01 UTC 2024
Sun Apr 14 07:00:01 UTC 2024
Mon Apr 15 07:00:01 UTC 2024
Tue Apr 16 07:00:01 UTC 2024
Wed Apr 17 07:00:01 UTC 2024
Thu Apr 18 07:00:01 UTC 2024
Fri Apr 19 07:00:01 UTC 2024
Sat Apr 20 07:00:01 UTC 2024
Sun Apr 21 07:00:01 UTC 2024
Mon Apr 22 07:00:01 UTC 2024
Tue Apr 23 07:00:01 UTC 2024
Wed Apr 24 07:00:01 UTC 2024
Thu Apr 25 07:00:01 UTC 2024
Fri Apr 26 07:00:01 UTC 2024
Sat Apr 27 07:00:01 UTC 2024
