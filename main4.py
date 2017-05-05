#import math

def main():
    """
    This function displays the home page of the EZHealth application and
    """

    print("Welcome to EZHealth \n \n We offer the following services:")
    print("\
        \n 1. Doctor lookup by location \
        \n 2. BMI calculator \
        \n 3. Healthy daily calorie intake calculator\
        \n 4. Recommended baby items checklist *Great for expecting/new parents!* \
        \n 5. Healthy daily sleep duration calculator")

    print("\n Type \"0\" to quit")

    mainMenuInput = (input("\n Please type the number of the service you'd like to explore: "))
    #while mainMenuInput.isdigit() == False:
    #    mainMenuInput = (input("\n Please type an integer between 1 and 7 and press Enter"))
    #    return

    while mainMenuInput != '0':
        if mainMenuInput.isdigit() == False: #error check if input is out of range
            mainMenuInput = input("Please type a number from 1 to 5: ")

        elif int(mainMenuInput) not in [1,2,3,4,5,6,7]:
            mainMenuInput = input("Please type a number from 1 to 5: ")

        elif int(mainMenuInput) == 1: #call each separate method function
            import doc_search #imports function
            doc_search.docs()
            repeat1 = input("Would you like to use this function again? (y/n)  ")
            while True:
                if repeat1 == 'y':
                    import doc_search
                    doc_search.docs()
                    repeat1 = input("Would you like to use this function again? (y/n)  ")
                elif repeat1 == 'n':
                    break
                else:
                    repeat1 = input("Please enter either \"y\" or \"n\".")
            break

        elif int(mainMenuInput) == 2:
            import bmi #imports function
            bmi.BMI()
            repeat2 = input("Would you like to use this function again? (y/n)  ")
            while True:
                if repeat2 == 'y':
                    import bmi
                    bmi.BMI()
                    repeat2 = input("Would you like to use this function again? (y/n)  ")
                elif repeat2 == 'n':
                    break
                else:
                    repeat2 = input("Please enter either \"y\" or \"n\".")
            break

        elif int(mainMenuInput) == 3:
            import caltesting
            caltesting.calorie_intake()
            repeat3 = input("Would you like to use this function again? (y/n)  ")
            while True:
                if repeat3 == 'y':
                    import caltesting
                    caltesting.calorie_intake()
                    repeat3 = input("Would you like to use this function again? (y/n)  ")
                elif repeat3 == 'n':
                    break
                else:
                    repeat3 = input("Please enter either \"y\" or \"n\".")
            break

        elif int(mainMenuInput) == 4:
            import essentials
            essentials.checklist()
            repeat4 = input("Would you like to use this function again? (y/n)  ")
            while True:
                if repeat4 == 'y':
                    import essentials
                    essentials.checklist()
                    repeat4 = input("Would you like to use this function again? (y/n)  ")
                elif repeat4 == 'n':
                    break
                else:
                    repeat4 = input("Please enter either \"y\" or \"n\".")
            break

        elif int(mainMenuInput) == 5:
            print('aloha')
            import sleepcal_alt
            sleepcal_alt.sleep()
            repeat5 = input("Would you like to use this function again? (y/n)  ")
            while True:
                if repeat5 == 'y':
                    import sleepcal_alt
                    sleepcal_alt.sleep()
                    repeat5 = input("Would you like to use this function again? (y/n)  ")
                elif repeat5 == 'n':
                    break
                else:
                    repeat5 = input("Please enter either \"y\" or \"n\".")
            break

        else:
            print('uhoh')
    return


if __name__ == "__main__":
    main()
    mainMenuReturn = input("\n Would you like to return to the main menu? (y/n)  ")
    while True:
        if mainMenuReturn == 'y':
            main()
            mainMenuReturn = ""
            mainMenuReturn= input("\n Would you like to return to the main menu? (y/n)  ")
        elif mainMenuReturn == 'n':
            print("Thanks for using EZHealth today!")
            break
        else: #if types in wrong
             mainMenuReturn = input("Please enter either \"y\" or \"n\".")
         #problem here where, on second time, it skips to this line bc of the else statement
