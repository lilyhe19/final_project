def sleep():
    '''
    This function puts out the recommended number of hours of sleep per night according to the guidelines
    set by The National Sleep Foundation. The output is formatted as a range of hours, as there is no
    perfect formula for determining how much sleep one should get, and these numbers are simply recommendations
    based on the newest sleep research.

    You can type in your/your child's age, and the function will give you a recommendation based on your input.
    This function does not give reliable recommendations for children under 1 year old.
    '''
    print("\n This program returns the recommended number of hours of sleep per night \
    \n according to the age-based guidelines set by The National Sleep Foundation. \
    \n Note: this calculator may not be accurate for infants and very young children (under the age of 1).")

    master= [{'age':[1,2],'hours':"11-14"},{'age':[3,4,5],'hours':"10-13"},{'age':[6,7,8,9,10,11,12,13],'hours':"9-11"},{'age':[14,15,16,17],'hours':"8-10"}]

    number = int(input("Please enter an age (between 1-17 years): "))

    for x in master:
        if number in x['age']:
            print("Your child should sleep " + str(x['hours']) + " hours." )


#if __name__ == "__main__":

    #print("\n This program returns the recommended number of hours of sleep per night \
    #\n according to the age-based guidelines set by The National Sleep Foundation. \
	#\n Note: this calculator may not be accurate for infants and very young children (under the age of 1).")
    #number = int(input("Please enter in an age (between 1-17 years): "))
    #final_answer = sleep(number)
    #print("Your child should sleep " + str(final_answer) + " hours.")
