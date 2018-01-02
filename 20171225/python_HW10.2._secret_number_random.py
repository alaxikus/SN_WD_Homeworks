import random

greeting = "Hello."
print greeting
print "*" * 20

def main():
    secret = random.randint(1, 20)

    while True:
        guess = int(raw_input("Which number do you guess (between 1 and 20)? "))
        if guess == secret:
            print "Congratulations! Your answer is correct. It's number %s." % secret
            break

        else:
            print "Your answer is incorrect."
            guess = raw_input("Try again? Type y or n: ")
            if guess == "y":
                print guess
            if guess == "n":
                break

if __name__ == "__main__":
    main()

print "Thank you and goodbye."