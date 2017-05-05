def BMI():
    '''
    Takes user input of height (in) and weight (lb) and returns the BMI.
    Standard BMI is the ratio of weight (kg) to height squared (cm).
    For US users, this function can use pounds and inches.
    '''

    print("\n This program will return your BMI, \
    \n as calculated by the standard BMI formula (ratio of weight (kg) to height squared (cm)) \
    \n Note: this calculator may not be accurate for infants and very young children.")


    height = input("height(inches):  ")

    
    while (height) == "0":  
            height = (input("Please input a nonzero integer for height:  "))


    weight = input("weight(pounds):  ")
    while (weight) == "0": 
            weight = (input("Please input a nonzero integer for weight:  "))
         
    #prevents input from being the wrong type (sourced code from user: jmichalicek @http://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number)
    if height.isdigit() == False or weight.isdigit() == False: 
        print("Oops! Looks like you didn't enter a number somewhere. Please start over. ")
        return


    hMetric = int(height) * .0254
    wKG = int(weight) * .453592  
    Bmi = wKG / (hMetric**2)
    print ("Your BMI is " + str(round(Bmi,2)))
