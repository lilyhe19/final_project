#import math

def main():
    """
    docstring
    """
    print("Welcome to EZHealth \n \n Here are your options:")
    print("\
        \n 1. Look up a doctor by location \
        \n 2. Calculate your BMI \
        \n 3. Calculate the number of calories you should consume for your age and weight\
        \n 4. Access the recommended baby items checklist to be prepared for almost any situation \
        \n 5. Sleep Calculator \
        \n 6. Weight Based Divided Dose Calculator \
        \n 7. Forum")

    print("\n Type \"0\" to quit")

    mainMenuInput = int(input("\n Please type the number of the option you'd like to explore: "))

    while int(mainMenuInput) != 0:
        if int(mainMenuInput) not in [1,2,3,4,5,6,7]: #error check if input is out of range
            mainMenuInput = input("Please type a number between 1 and 4: ")

        elif mainMenuInput == 1: #call each separate method function
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

        elif mainMenuInput == 2:
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

        elif mainMenuInput == 3:
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

        elif mainMenuInput == 4:
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

        elif mainMenuInput == 5:
            import sleepcal
            sleepcal.sleep()
            repeat5 = input("Would you like to use this function again? (y/n)  ")
            while True:
                if repeat5 == 'y':
                    import sleepcal
                    sleepcal.sleep()
                    repeat5 = input("Would you like to use this function again? (y/n)  ")
                elif repeat5 == 'n':
                    break
                else:
                    repeat5 = input("Please enter either \"y\" or \"n\".")
            break

        elif mainMenuInput == 6:
            pass

        elif mainMenuInput == 7:
            pass
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
