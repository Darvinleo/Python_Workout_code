from random import randint


def guess_game():
    """
        Program choose random int from 1 to 100 and user need to guess it
        Program makes hints ( too low | to hi ) User have 5 attempts.
    """
    answer = randint(0, 100)
    attempts = 0
    print(f"\nI'm thinking of a number from one to 100  |  "
          f"Guess it, if you can :)"
          f"\nYou have {5 - attempts} attempts")
    while attempts < 5:
        try:
            guess = int(input("\nEnter your number here:  "))
            if guess == answer:
                print(f"Flawless Victory!! Number was {answer}")
                return
            if guess > answer:
                attempts += 1
                print(
                    f"Nope {guess} is too high\n{5 - attempts} "
                    "attempts left ")
            elif guess < answer:
                attempts += 1
                print(f"Nope {guess} is too low\n{5 - attempts} "
                      "attempts left ")
        except ValueError:
            print("Please enter only numbers...")
    print("You have used all the attempts, maybe next time...")


guess_game()
