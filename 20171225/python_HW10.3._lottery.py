import random

greeting = "Welcome to the Lottery numbers generator."
print greeting
print "*" * 20

def get_lottery_numbers(quantity):
    user_numbers = []

    while True:
        if len(user_numbers) == quantity:
            break

        numbers = random.randint(1, 45)

        if numbers not in user_numbers:
            user_numbers.append(numbers)

    return user_numbers

def main():
    numbers_question = raw_input("How many random numbers would you like to have (between 1 and 45): ")

    quantity_numbers = int(numbers_question)
    print get_lottery_numbers(quantity_numbers)

    print "Thank you and goodbye. Good luck!"

if __name__ == "__main__":
    main()
