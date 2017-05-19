def error(x):
    """
    docstring
    """

    while True:
        if x == 1:
        repeat1 = input("Would you like to use this function again? (y/n)  ")
        if repeat1 == 'y':
            import doc_search
            doc_search.docs()
            repeat1 = input("Would you like to use this function again? (y/n)  ")
        elif repeat1 == 'n':
            break
        else:
            repeat1 = input("Please enter either \"y\" or \"n\".")
            break

    while True:
        if x == 2:
            repeat2 = input("Would you like to use this function again? (y/n)  ")
            if repeat2 == 'y':
                import bmi
                bmi.BMI()
                repeat2 = input("Would you like to use this function again? (y/n)  ")
            elif repeat2 == 'n':
                break
            else:
                repeat2 = input("Please enter either \"y\" or \"n\".")
        break

    while True:
        if x == 3:
            repeat3 = input("Would you like to use this function again? (y/n)  ")
            if repeat3 == 'y':
                import calcounter_alt
                calcounter_alt.calorie_intake()
                repeat3 = input("Would you like to use this function again? (y/n)  ")
            elif repeat3 == 'n':
                break
            else:
                repeat3 = input("Please enter either \"y\" or \"n\".")
        break

    while True:
        if x == 4:
            repeat3 = input("Would you like to use this function again? (y/n)  ")
            if repeat4 == 'y':
                import essentials
                essentials.checklist()
                repeat4 = input("Would you like to use this function again? (y/n)  ")
            elif repeat4 == 'n':
                break
            else:
                repeat4 = input("Please enter either \"y\" or \"n\".")

    while True:
        if x == 5:
            repeat5 = input("Would you like to use this function again? (y/n)  ")
            if repeat5 == 'y':
                import sleepcal_alt
                sleepcal_alt.sleep()
                repeat5 = input("Would you like to use this function again? (y/n)  ")
            elif repeat5 == 'n':
                break
            else:
                repeat5 = input("Please enter either \"y\" or \"n\".")
        break

    while True:
        if x == 6:
            pass

    while True:
        if x == 7:
            pass

    return

    print("hello")
