def sleep():
    '''
    This function puts out the recommended number of hours of sleep per night according to the guidelines
    set by The National Sleep Foundation. The output is formatted as a range of hours, as there is no
    perfect formula for determining how much sleep one should get, and these numbers are simply recommendations
    based on the newest sleep research.

    You can type in you/your child's age, and the function will give you a recommendation based on your input.
    This function does not give reliable recommendations for children under 1 year old.
    '''

    print("\n This program returns the recommended number of hours of sleep per night \
    \n according to the age-based guidelines set by The National Sleep Foundation. \
	\n Note: this calculator may not be accurate for infants and very young children.")

    age = (input("Please enter an age (in years): "))

    #prevents input from being the wrong type (sourced code from user: jmichalicek @http://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number)
    while age.isdigit() == False: 
        age = input("Error, please enter a positive integer: ")


    number = int(age)

    while number < 0: 
        number = input("Please enter an age greater than 0:  ")

    if 0 <= number < 3:
        rec_hr = '11-14'
    elif 3 <= number < 6:
        rec_hr = '10-13'
    elif 6 <= number < 14:
        rec_hr = '9-11'
    elif 14 <= number < 18:
        rec_hr = '8-10'
    elif 18 <= number < 65:
        rec_hr = '7-9'
    elif 65 <= number:
        rec_hr = '7-8'
    print("You/your child should sleep", str(rec_hr), "hours every night.")


#if __name__ == "__main__":

#    print("This program will tell you how many hours your child should sleep based on his/her age.")
#    print("This program does apply to infants (children under one year old)")
#    number = int(input("Please enter in an age (1-17 years): "))
#    print("Your child should sleep " + str(rec_hr) + " hours.")
