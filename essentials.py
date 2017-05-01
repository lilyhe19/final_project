def checklist():

    print("\n This program returns a checklist of the top ten items you will need to care for your infant")

    items= [
    ["()", 1 , "Baby formula and bottle"], ["()", 2, "Diapers"], ["()", 3, "Baby soap and towel"],
    ["()", 4, "First aid kit"], ["()", 5, "Blanket"], ["()", 6, "Onesie"], ["()", 7, "Pacifier"],
    ["()", 8, "Baby carrier"], ["()", 9, "Carseat"], ["()", 10, "Crib"]
        ]

    print(items)

    checked = int(input("To check off an item, please enter the corresponding number items you already have (one number at a time only). \n >>"))

    newlist= [ ]
    for [a,b,c] in items:
        if checked == b:
            a = '(x)'
            y= [a,b,c]
    newlist= newlist + [y]
    print(newlist)

#y= ['(x)' for a in [a,b,c] if checked == b]

#newlist= [ ]
#for [a,b,c] in items:
    #if checked == b:
        #y= ['(X)' for a in [a,b,c]]
#newlist= newlist + [y]
#return newlist
