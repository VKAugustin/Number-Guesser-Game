import random 

while True:
    top_of_range = input("Type a Number: ")


    if top_of_range.isdigit():# if it's a Digit
        top_of_range = int(top_of_range)

        #Smaller Number
        if top_of_range <= 0:
            print("Please Type a Number larger than 0 Next time!")
            continue
    #if it's Not a Number
    else:
        print("Please type a Number Next time!")
        continue

    random_number = random.randint(0, top_of_range)
    guesses = 0

    while True:
        guesses +=1
        user_guess = input("Make a guess: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Please type a Number next time!")
            continue

        if user_guess == random_number:
            print("You got it!")
            break
        elif user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")

    print("You got in", guesses, "guesses")
    print("")
    repeat = input("Do you want another Game? ")

    if repeat.lower().strip() != "yes":
        quit()
    else:
        continue