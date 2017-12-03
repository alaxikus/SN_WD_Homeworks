while True:
    secret = 77
    guess = raw_input("Which number do you guess? ")
    if guess == secret:
        print "Congratulations! Your answer is correct."
    if guess is not secret:
        print "Your answer is incorrect."
        print "Try again? Type y or n"
    if guess == "y":
        print guess
    if guess == "n":
        break
