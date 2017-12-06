secret = "77"

while True:
    guess = raw_input("Which number do you guess? ")
    if guess == secret:
        print "Congratulations! Your answer is correct."
        break
    else:
        print "Your answer is incorrect."
        guess = raw_input("Try again? Type y or n: ")
        if guess == "y":
            print guess
        if guess == "n":
            break
