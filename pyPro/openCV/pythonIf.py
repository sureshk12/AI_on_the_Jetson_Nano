while True:
    number = float(input("Please enter your number : "))
    if number > 0 and number%2 == 0 :
        print("Your number was positive")
        print("And your number is even")
        print("Thanks for playing")
    if number > 0 and number%2 != 0 :
        print("Your number was positive")
        print("And your number is odd")
        print("Thanks for playing")
    if number < 0 and number%2 == 0 :
        print("Your number was negative")
        print("And your number is even")
        print("Thanks for playing")
    if number < 0 and number%2 != 0 :
        print("Your number was negative")
        print("And your number is odd")
        print("Thanks for playing")
    if number == 0:
        print("Your number is Zero")
        print("Thanks for playing")