# user enters a number
# if the number is divisble by three, print "fizz"
# if the number is divisble by five, print "buzz"
# if the number is divisble by three and five, print "fizzbuzz"
# end at the entered number


print "Welcome to FizzBuzz"
print "*" * 20

end = raw_input("Please enter a number between 1 and 100: ")

try:
    end = int(end)

    for number in range(1,end +1):

        if number % 3 == 0:
            print "fizz"

# wenn die Zahl durch fuenf teilbar ist, dann print "buzz"
        elif number % 5 == 0:
            print "buzz"

# wenn die Zahl durch drei und fuenf teilbar ist, dann print "fizzbuzz"
        elif number % 3 == 0 and number % 5 == 0:
            print "fizzbuzz"

        else:
            print number

except:
    print "Sorry, you didn't enter a number."