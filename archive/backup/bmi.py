def BMI():
    '''
    Takes user input of height (in) and weight (lb) and returns the BMI.
    Standard BMI is the ratio of weight (kg) to height squared (cm).
    For US users, this function can use pounds and inches.
    '''

    print("\n This program will return your BMI, \
    \n as calculated by the standard BMI formula (ratio of weight (kg) to height squared (cm)) \
    \n Note: this calculator may not be accurate for infants and very young children.")

#kilograms and centimeters
#    height = input("height >> ")
#    weight = input("weight >> ")
#    hMetric = int(height)
#    wKG = int(weight)
#    bmi = wKG /(hMetric**2)
#    return bmi

#pounds and inches
    height = input("height(inches)>> ")
    weight = input("weight(pounds)>> ")

    #prevents input from being the wrong type (sourced code from user: jmichalicek @http://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number)
    while height.isdigit() == False or weight.isdigit() == False: 
        print("Oops! Looks like you didn't enter a number somewhere. Please start over")
        return

    #prevents denominator from being 0, and unrealistic answer 
    while int(height) == 0 or int(weight) == 0: 
        if height == 0: 
            height = int(input("Please input a nonzero integer for height>> "))
        else: 
            weight = int(input("Please input a nonzero integer for weight>> "))
    hMetric = int(height) * .0254 #convert to inches
    wKG = int(weight) * .453592 #convert to kilograms 
    Bmi = wKG / (hMetric**2)
    print ("Your BMI is " + str(round(Bmi,2)))

#if __name__ == "__main__":
#Intro
#Prompt
#    print("Let's calculate your BMI! \
#    \n At the prompt, type in only the numbers that quantifies your height or weight, and round off to the nearets whole number\
#    \n ")
#Prints the answer
#    print("Your BMI is", BMI())
