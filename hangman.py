def hangman_game():

    name = input("What is your name?")
    print("Hello, " + name, "It is time to play HamgMan")
    print("Start Guessing...")
    # Determine the Number of turns
    turns = 10
    # Creats a variable with an empty value
    guesses = ""
    # Here we set the Secret
    word = "secret"

    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1
        if failed == 0:
            print("\nYou WON!     :)")
            break
        guess = input("\nGuess a Character : ")
        guesses += guess
        if (guess not in word):
            turns -= 1
            print("\nWrong Guess :/")
        print("\nYou have ", + turns, "more guesses")
        if turns == 0:
            print("\nGame is OVER, you LOST :o")
    check = input("\nDo you want to play again Y/N?")
    if check == "Y":
        hangman_game()
hangman_game()
