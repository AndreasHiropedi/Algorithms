def guessMyNumber():
    print("Let's play a game: enter a number between 1 and 100 and I will guess it in at most 10 attempts.")
    print("After every try, you have to tell me if the number i guessed was higher or lower than the number u chose")
    number = int(input("Please enter a number between 1 and 100: "))
    tries_left = 10
    guessed = False
    upper = 101
    guess = 50
    lower = 1
    while guessed == False:
        if tries_left == 0:
            print("You won")
        answer = input("Is your number " + str(guess) + "? (enter Y for yes or N for no) ")
        tries_left = tries_left - 1
        if answer == "Y":
            guessed = True
            print("I won")
            print("I had " + str(tries_left) + " guesses left")
        else:
            user_info = input("Was it higher or lower (enter H for Higher and L for Lower): ")
            if user_info == "H":
                lower = guess
                guess = (upper + lower)//2
            elif user_info == "L":
                upper = guess
                guess = (upper + lower)//2
guessMyNumber()
            
    
