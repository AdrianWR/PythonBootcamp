from random import randint


def guess_input(target):
    count = 1
    guess = 0
    while (guess != target):
        try:
            guess = input("What's your guess between 1 and 99?\n")
            guess = int(guess)
        except ValueError:
            if guess == 'exit':
                guess = target
                count = 0
            else:
                print("That's not a number.")
        except KeyboardInterrupt:
            print("\n")
            guess = target
            count = 0
        else:
            if guess == target:
                if target == 42:
                    print("The answer to the ultimate question of " +
                          "life, the universe and everything is 42.")
                else:
                    print("Congratulations, you've got it!")
            elif guess > target:
                print("Too high!")
                count += 1
            elif guess < target:
                print("Too low!")
                count += 1
    return count


def main():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 " +
          "to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")
    target = randint(1, 99)
    result = guess_input(target)
    if result > 1:
        print(f"You won in {result} attempts!")
    elif result == 1:
        print("Congratulations! You got it on your first try!")
    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()
