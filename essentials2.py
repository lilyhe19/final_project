def checklist():

    print("\n This program returns a checklist of the top ten items you will need to care for your infant")

    items= [
    ["() ", 1 , "Baby formula and bottle"], 
    ["() ", 2, "Diapers"], ["() ", 3, "Baby soap and towel"],
    ["() ", 4, "First aid kit"], ["() ", 5, "Blanket"], ["() ", 6, "Onesie"], ["() ", 7, "Pacifier"],
    ["() ", 8, "Baby carrier"], ["() ", 9, "Carseat"], ["() ", 10, "Crib"]
        ]

    for line in items: #sourced the *line code from user: Jim Farasakis Hilliard @http://stackoverflow.com/questions/38872341/print-list-of-lists-in-separate-lines
        print(*line) 

    nums = [ ]
    numbs = input("To check off certain items, please input a list of the corresponding numbers (separated by commas only), then hit Enter. \n >>")
    
    #hasBUGS
    #prevents input from being the wrong type (sourced code from user: jmichalicek @http://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number)
    while numbs.isdigit() == False and numbs != ",": 
        print("Oops! Looks like you didn't enter a number somewhere. Please start over")
        return

    numbs = numbs.split(",")
    for x in numbs:
        if isinstance(int(x), int):
            nums.append(int(x))

    for z in nums: #iterate through the inputed list
        for k in items: #access original full list 
            if k[1] == z: #compare if it is in original list 
                k[0] = '(X)' #replace empty with X 
            else: 
                k[0] == '() '
    for line in items: #sourced the *line code from user: Jim Farasakis Hilliard @http://stackoverflow.com/questions/38872341/print-list-of-lists-in-separate-lines
        print(*line)

#y= ['(x)' for a in [a,b,c] if checked == b]

#newlist= [ ]
#for [a,b,c] in items:
    #if checked == b:
        #y= ['(X)' for a in [a,b,c]]
#newlist= newlist + [y]
#return newlist
