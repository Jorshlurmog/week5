import random

# User random number guess


def guess_random_number(tries, start, stop):
    target = random.randint(start, stop + 1)
    print(target)
    while tries != 0:
        print(f"Tries remaining: {tries}")
        guess = input("Guess a number between 0 and 10: ")
        if int(guess) == target:
            print("You guessed the correct number!")
            return
        elif int(guess) < target:
            print("Guess a higher number!")
        elif int(guess) > target:
            print("Guess a lower number!")
        tries -= 1
    print("\nYou failed to guess the correct number!")


guess_random_number(5, 0, 10)

# Computer random number guess with linear search


def guess_random_num_linear(tries, start, stop):
    target = random.randint(start, stop + 1)
    print(f"The number for the program to guess is: {target}")
    for x in range(start, stop + 1):
        print(f"The program is guessing...{x}")
        if x == target:
            print("\nThe program has guessed the correct number!")
            break
        else:
            tries -= 1
            print(f"Number of tries left: {tries}")
            if tries == 0:
                print("\nThe program has failed to guess the correct number!")
                break


guess_random_num_linear(5, 0, 10)

# Computer random number guess with binary search


def guess_random_num_binary(tries, start, stop):
    target = random.randint(start, stop + 1)
    print(f"The number for the program to guess is: {target}")
    numbers = []
    for number in range(start, stop + 1):
        numbers.append(number)
    while start <= stop:
        while tries > 0:
            pivot = (start + stop) // 2
            pivot_value = numbers[pivot]
            print(f"The program is guessing...{pivot}")

            if pivot_value == target:
                print("\nThe program has guessed the correct number!")
                return pivot
            if pivot_value > target:
                print("Not the correct number. Guessing lower!")
                stop = pivot - 1
                tries -= 1
            else:
                print("Not the correct number. Guessing higher!")
                start = pivot + 1
                tries -= 1

            print(f"Tries left: {tries}")
        print("\nThe program has failed to guess the correct number!")
        return -1


guess_random_num_binary(5, 0, 100)
