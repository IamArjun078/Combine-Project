
###################################################### Game Function###########################################################################
def game_menu():
    import random
    game_character = ["s", "p", "c"]
    import datetime
    ###############################Making Date Function #############
    def gettime():
        import datetime
        return datetime.datetime.now()

    ##################### Selecting Game ##############################
    try:
        name = str(input("Enter Your Name\n"))
    except Exception as error:
        print(error)
    print(f"{name} Please Select The Game\n1.Stone Paper Scissor\n2.Guessing Number\n3.Open Leader Board\nAs 1, 2 and 3\nmm For Main Menu\n")
    try:
        game = str(input("Enter Game No\n"))
    except Exception as error:
        print(error)
    #################################Stone Paper Scissor#########################
    if game == "1":
        with open("SPS-Score.txt", "a") as op:
            op.write(str([str(gettime())]) + ": " + name + "\n")
        print(f"{name} Welcome to the Game\nYou Have 10 Lfe To win From Pc\nChoices are Stone(s),Paper(p),Scissor(c)")
        life = 0
        no_of_life = 10
        ###################point area###############################
        player_score = 0
        computer_score = 0
        ################### Gaming Area ###########################
        while life < no_of_life:
            player_choice = input("Enter Your Choice as s,p,c\n")
            computer_choice = random.choice(game_character)
            if computer_choice == player_choice:
                print("Tie\n")
                print(f"{name} Your Score is {player_score}\nComputer Score is {computer_score}")
            elif computer_choice == "c" and player_choice == "p":
                print("You Lose :(")
                print("Computer Thinks Scissor ")
                computer_score += 1
                print(f"{name} Your Score is {player_score}\nComputer Score {computer_score}")
            elif computer_choice == "p" and player_choice == "c":
                print("You Win :)")
                print("Computer Thinks Paper")
                player_score += 1
                print(f"{name} Your Score is {player_score}\nComputer Score {computer_score}")
            elif computer_choice == "s" and player_choice == "c":
                print("You Lose :(")
                print("Computer Thinks Stone")
                computer_score += 1
                print(f"{name} Your Score is {player_score}\nComputer Score {computer_score}")
            elif computer_choice == "c" and player_choice == "s":
                print("You Win :)")
                print("Computer Thinks Scissor")
                player_score += 1
                print(f"{name} Your Score is {player_score}\nComputer Score is {computer_score}")
            elif computer_choice == "p" and player_choice == "s":
                print("You Lose :(")
                print("Computer Thinks Paper")
                computer_score += 1
                print(f"{name} Your Score is {player_score}\nComputer Score is {computer_score}")
            elif computer_choice == "s" and player_choice == "p":
                print("You Win :)")
                print("Computer Thinks Stone")
                player_score += 1
                print(f"{name} Your Score is {player_score}\nComputer Score is {computer_score}")
            else:
                print("Please Enter Correct Option")
            life = life + 1
            print(f"{name} Life Left:{no_of_life - life}")
        #######################################Leader Board####################################

        winning_score = player_score - computer_score  ############## Will be use to append the winning point in the file #
        loosing_score = computer_score - player_score  ############## Will be use to append the loosing point in the file #
        ######################################################################################
        if computer_score == player_score:
            print(f"{name} Match Ties Between You and Computer")
            with open("SPS-Score.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + name + " Result= Tie")
        elif player_score > computer_score:
            print(f"{name} You Wins by {player_score - computer_score} scores from Computer")
            with open("SPS-Score.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + name + " Result= Win" + " Wonned by " + str(
                    winning_score) + " Points From Computer")
        else:
            print(f"{name} you lose from Computer from {computer_score - player_score} scores")
            with open("SPS-Score.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + name + " Result= Lose" + " Lose by " + str(
                    loosing_score) + " Points From Computer")
    #################################### Guessing Number####################################
    elif game == "2":
        guessing_number = 17
        life = 0
        no_of_life = 6
        while life < no_of_life:
            try:
                number = int(input("Please Enter The Number You Guessed\nMust be Between 0-40\n"))
            except Exception as error:
                print(error)

            if number == guessing_number:
                print(f"{name} You Win :)")
                with open("Guessing.txt", "a") as op:
                    op.write(str([str(gettime())]) + ":" + name + " Result: Win")
                break
            elif number > guessing_number:
                print(f"{name} Please Guess a Smaller Number")
            elif number < guessing_number:
                print(f"{name} Please Guess a Bigger Number")
            else:
                print(f"Game Over")
            life = life + 1
            print(f"{name} life left: {no_of_life - life}")
    ############################################### Opening The Leader Board #########################
    if game == "3":
        leader_board = int(input("1 For Stone Paper Game\n2 For Guessing No Game\n"))
        if leader_board == 1:
            f = open("SPS-Score.txt")
            r = f.read()
            print(r)
        else:
            f = open("Guessing.txt")
            r = f.read()
            print(r)
    elif game == "mm":
        main_menu()
    menu_selection = str(input("Enter gm if you want to enter in Game Menu\nPress mm to enter in MainMenu\nq to exit\n"))
    if menu_selection == "gm":
        game_menu()
    elif menu_selection == "mm":
        main_menu()
    elif menu_selection == "q":
        exit()
    else:
        print("Please Enter Valid Value\n")
        game_menu()
################################################ Game Ended ###############################################################################################

############################################### Calculator Part ##########################################################################################
def calculator_menu():
    add = lambda x, y: x + y
    minus = lambda x, y: x - y
    division = lambda x, y: x / y
    multiplication = lambda x, y: x * y
    power = lambda x, y: x ** y

    ######################  Calculator Part            ###############################################
    print("1.Addition(+)\n2.Subtraction(-)\n3.Multiplication(*)\n4.Division(/)\n5.Power(**)\n6. mm For Main Menu ")
    try:
        operation = input("Enter the operation You Want to Perform\n")
    except Exception as error:
        print(error)
    if operation == "+":
        number_1 = float(input("Enter 1st Number\n"))
        number_2 = float(input("Enter 2nd Number\n"))
        print(f"The sum of {number_1} and {number_2} is: ", add(number_1, number_2))
    elif operation == "-":
        number_1 = float(input("Enter 1st Number\n"))
        number_2 = float(input("Enter 2nd Number\n"))
        print(f"The difference of {number_1} and {number_2} is: ", minus(number_1, number_2))
    elif operation == "*":
        number_1 = float(input("Enter 1st Number\n"))
        number_2 = float(input("Enter 2nd Number\n"))
        print(f"The product of {number_1} and {number_2} is: ", multiplication(number_1, number_2))

    elif operation == "/":
        number_1 = float(input("Enter 1st Number\n"))
        number_2 = float(input("Enter 2nd Number\n"))
        print(f"The division of {number_1} and {number_2} is: ", divide(number_1, number_2))
    elif operation == "**":
        number_1 = float(input("Enter Number\n"))
        number_2 = float(input("Enter How Much Power You want to raise\n"))
        print(f"The power of {number_1} rasie to power {number_2} is: ", power(number_1, number_2))
    elif operation == "6":
        main_menu()
    else:
        print("Thank You For Using\n")
    menu_selection = str(input("Enter cm if you want to enter in Game Menu\nPress mm to enter in MainMenu\nq to exit\n"))
    if menu_selection == "cm":
        calculator_menu()
    elif menu_selection == "mm":
        main_menu()
    elif menu_selection == "q":
        exit()
    else:
        print("Please Enter Valid Value\n")
        calculator_menu()

##################################      Calculator Done       #####################################################

def fibonacci_factorial_menu():
    ######## 0 1 1 2 3 5 8 13...etc these are fibonacci number the next number is the sum of first two number  #############

                     ########### creating function of Fibonacci number ##########################
    def fibonacci(n):                           ###### n bcz fibonaci are of natural number, now by seeing fibonaci series#
         if n == 1:
             return 0                            ######### as first term in fibonacci series is 0 ##########################
         elif n == 2:
             return 1                            ######## as 2nd term in fibonacci series is 1    ##########################
         else:
             return fibonacci(n-1) + fibonacci(n-2)   ## for any other other value of n expcet 1 or 2 it will add first two fibonaccci no#



                           ################ recursive method ############################################

    def factorial_resursive(n):
        if n == 1:
            return 1
        else:
            return n * factorial_resursive(n-1)

    print("Select Operation as 1,2 and 3\n")
    select_operation = int(input("1.Fibonacci Finder\n2.Factorial Calculator\n3.For quit\n"))
    while select_operation != 3:
        if select_operation == 1:
            number = int(input("Enter which fibonacci you want to find\n"))
            print(f"The {number} fibonacci number is: ", fibonacci(number))
        elif select_operation == 2:
            number = int(input("Enter the number of which factorial you want to find\n"))
            print(f"The factorial of {number} is: ", factorial_iterative(number))
        else:
            print("Thank You For Using\n")

    menu_selection = str(input("Enter cm if you want to enter in Game Menu\nPress mm to enter in MainMenu\nq to exit\n"))
    if menu_selection == "fm":
        fibonacci_factorial_menu()
    elif menu_selection == "mm":
        main_menu()
    elif menu_selection == "q":
        exit()
    else:
        print("Please Enter Valid Value\n")
        fibonacci_factorial_menu()

##################################### Factorial And Fibonacci Done #####################################################

################################### Astrologers Star #############################################################
def astrologers_star():
    try:
        star_type = str(input("1 For Increasing Star Pattern\n2 For Decreassing Star Pattern\n  mm for Main Menu\n"))
    except Exception as error:
        print(error)
    if star_type == "1":
        try:
            star_value = int(input("Enter The Number Of Row You Wanr\n"))
        except Exception as error:
            print(error)
        for i in range(0,star_value+1):
            print("*"*int(i))
    elif star_type == "2":
        try:
            star_value = int(input("Enter The Number Of Row You Want\n"))
        except Exception as error:
            print(error)
        for i in range(star_value+1, 0, -1):
            print("*" * int(i))
    elif star_type == "mm":
        main_menu()
    else:
        print("Please Enter A Valid Value\n")
        astrologers_star()
    menu_selection = str(input("Enter asm if you want to enter in Astorologer Star Menu\nPress mm to enter in MainMenu\nq to exit\n"))
    if menu_selection == "asm":
        astrologers_star()
    elif menu_selection == "mm":
        main_menu()
    elif menu_selection == "q":
        exit()
    else:
        print("Please Enter Valid Value\n")
        astrologers_star()

##################################### Diet Chart  ###################################################################




################################# Numeric Table Maker #############################################################
def table_menu():
    main_menu = str(input("Enter mm For Main Menu\n"))
    x = int(input("Enter The Number Of Which Table You Want\n"))


                   ###################### Function for Multiplying The Values ###########################
    def table(n):
        return n * i ######################3 i is taken from for loop as a range ################################

    """
                                I have divided It Into Two parts
                                1. The range is fixed it will calculate table from  1 to 10 as normally we found
                                2. You can enter Range Manusally from where to where You want to Calculate Table

                                            by Rakesh Dhariwal
    """
    range_selector = int(input("Please Select The Range From Where To Where U To Multiply\n1.Fixed Range(1-10)\n2.Enter Ending And Starting Point Manually\n"))

                        ##################### Applying The loops ##############################

    if range_selector == 1:
        print(f"The Table Of {x} is: ")
        for i in range(1, 11):
            print(f"{x} x {i}   =  ", table(x))
    elif range_selector == 2:
        print(f"The Table Of {x} is: ")
        for i in range(int(input("Starting Point Of Table\n")), int(input("Enter The Ending Point Of Table\n")) + 1):
            print(f"{x} x {i}  =  ", table(x))
    else:
        main_menu()
    menu_selection = str(input("Enter tm if you want to enter in Table Maker Menu\nPress mm to enter in MainMenu\n"))
    if menu_selection == "tm":
        table_menu()
    elif menu_selection == "mm":
        main_menu()
    else:
        print("Please Enter Valid Value\n")
        table_menu()

############################################### Main Menu ###########################################################
def main_menu():
    intro = "Welcome! To The All In One Project\nConsist OF Games, Calculator, Fibonacci, Factorial, Star Maker,Numeric Table Finder\n"
    print(intro)
    start = input("Press Any Key To Continue\n")
    if start != "@#$":
        try:
            menu_selection = int(input("1.Games, 2.Calculator, 3.Fibonacci & Factorial, 4.Astrologer Star Pattern,5.Numeric Table Finder\nSelect as 1, 2, 3 ...5\n"))
        except Exception as error:
            print(error)

        if menu_selection == 1:
            game_menu()
        elif menu_selection == 2:
            calculator_menu()
        elif menu_selection == 3:
            fibonacci_factorial_menu()
        elif menu_selection == 4:
            astrologers_star()
        elif menu_selection == 5:
            table_menu()
    else:
        print("Please Enter Valid Input\n")

    main_menu()

main_menu()
################################################ Rakesh Dhariwal ######################################################
