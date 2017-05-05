def checklist():
    '''
    Displays a general checklist of important items.
    User inputs the items that they have.
    Prints new list with the items checked off.
    '''

    print("\n This program returns a checklist of the top ten items you will need to care for your infant")

    items= [
    ["() ", 1 , "Baby formula and bottle"],["() ", 2, "Diapers"], ["() ", 3, "Baby soap and towel"],
    ["() ", 4, "First aid kit"], ["() ", 5, "Blanket"], ["() ", 6, "Onesie"], ["() ", 7, "Pacifier"],
    ["() ", 8, "Baby carrier"], ["() ", 9, "Carseat"], ["() ", 10, "Crib"]
        ]

    for line in items: #sourced the *line code from user: Jim Farasakis Hilliard @http://stackoverflow.com/questions/38872341/print-list-of-lists-in-separate-lines
        print(*line)

    print("Input each number, then hit Enter, \n until you reach the end, at which point type in '-1' and hit Enter again")
    nums,p,loop = [],0,True
    while loop:
        num = input("Enter the number corresponding to the item you'd like to check off here:  ")
        p = p + 1
        if num == '-1':
            loop = False
        elif num.isdigit() == False: #prevents input from being the wrong type
            print("Oops! Looks like you didn't enter a number. Please start over. ")
            return
        elif isinstance(int(num), int) == True:
            nums.append(int(num))
            
    for z in nums: #iterate through the inputted list
        for k in items: #access original full list
            if k[1] == z: #compare if it is in original list
                k[0] = '(X)' #replace empty with X

    for line in items: #sourced the *line code from user: Jim Farasakis Hilliard @http://stackoverflow.com/questions/38872341/print-list-of-lists-in-separate-lines
        print(*line)
