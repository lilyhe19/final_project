def BMI():
	'''
	Takes user input of height (in) and weight (lb) and returns the BMI.
	Standard BMI is the ratio of weight (kg) to height squared (cm).
	For US users, this function can use pounds and inches.
	'''
#kilograms and centimeters
#	height = input("height >> ")
#	weight = input("weight >> ")
#	hMetric = height
#	wKG = weight
#	bmi = wKG / (hMetric*hMetric)
#	return bmi

#pounds and inches
	height = int(input("height(inches)>> "))
	weight = int(input("weight(pounds)>> "))
	hMetric = height * .025 #convert to inches
	wKG = weight * .45
	bmi = wKG / (hMetric*hMetric)
	return bmi

if __name__ == "__main__":
#Intro
#Prompt
	print("Using this function, you can calculate your BMI \
	\n At the prompt, type in only the number that quantifies your height or weight\
	\n ")
#Prints the answer
	print("Your BMI is", bmi())
