def checklist():

    print("\n This program returns a checklist of the top ten items you will need to care for your infant")

    items= [
    ["()", 1 , "Baby formula and bottle"], ["()", 2, "Diapers"], ["()", 3, "Baby soap and towel"],
    ["()", 4, "First aid kit"], ["()", 5, "Blanket"], ["()", 6, "Onesie"], ["()", 7, "Pacifier"],
    ["()", 8, "Baby carrier"], ["()", 9, "Carseat"], ["()", 10, "Crib"]
        ]

    print(items)

    nums = [int(x) for x in numbs if isinstance(int(x), int)]
    numbs = input("To check off certain items, please input a list of the corresponding numbers (separated by commas only), then hit Enter. \n >>")
    numbs = numbs.split(",")
           

    for z in nums:
        for k in items:
            if k[1] == z:
                k[0] = '(x)'
    return print(items)

#y= ['(x)' for a in [a,b,c] if checked == b]

#newlist= [ ]
#for [a,b,c] in items:
    #if checked == b:
        #y= ['(X)' for a in [a,b,c]]
#newlist= newlist + [y]
#return newlist
