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
#	height = input("height >> ")
#	weight = input("weight >> ")
#	hMetric = int(height)
#	wKG = int(weight)
#	bmi = wKG /(hMetric**2)
#	return bmi

#pounds and inches
	height = input("height(inches)>> ")
	weight = input("weight(pounds)>> ")
	hMetric = int(height) * .025 #convert to inches
	wKG = int(weight) * .45
	Bmi = wKG / (hMetric**2)
	return print("Your BMI is", round(Bmi,1))

#if __name__ == "__main__":
#Intro
#Prompt
#	print("Let's calculate your BMI! \
#	\n At the prompt, type in only the numbers that quantifies your height or weight, and round off to the nearets whole number\
#	\n ")
#Prints the answer
#	print("Your BMI is", BMI())
