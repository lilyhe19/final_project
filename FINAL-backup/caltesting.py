def calorie_intake():
	'''
    This function calculates the number calories one should consume
    on a daily basis using Harris Benedict BMR equation,
    given a person's weight, height, age, and birth gender.
    '''

	print("This program will calculate number of calories you should consume per day.")
	print("Please note this calculator may not be accurate for infants and young children.")

	#while gender != "male" or gender != "female":
	#gender= input("Error, please type in gender again")

	# weight= float(input("How much do you weigh in pounds?>> "))
	# height= float(input("How tall are you in inches?>> "))
	# age= float(input("How many years old are you?>> "))
	# gender = input("Please type in gender: ")
	# answer = 0

	gender = input("Please type in your birth gender (male/female):  ")

	while gender != "male" and gender != "female":
		gender = input("Error, please type in gender again>> ")

	w = input("How much do you weigh? (pounds):  ")
	h = input("How tall are you? (inches):  ")
	years = input("How old are you? (years):  ")

	#prevents input from being the wrong type (sourced code from user: jmichalicek @http://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number)
	while w.isdigit() == False or h.isdigit() == False or years.isdigit() == False:
		print("Oops! Looks like you didn't enter a number somewhere. Please start over. ")
		return

	weight = int(w)
	height = int(h)
	age = int(years)

	if gender == "male":
		x_male = 66+6.2*(float(weight))+12.7*(float(height))-6.76*(float(age))
		answer = x_male
	else:
		x_female = 655.1+4.35*(weight)+4.7*(height)-4.7*(age)
		answer = x_female

	# while True: #use "is not" to compare strings
	# #print(gender)
	# 	gender = input("Error, please type in gender again")
	# 	if gender != "male" or "female":
	# 		print(gender)
	# 		print(gender=="male")
	# 		gender=''
	# 	elif gender== "male":
	# 		x_male= 66+6.2*(weight)+12.7*(height)-6.76*(age)
	# 		answer = x_male
	# 		#x_male is number of calories a male should consume
	# 	elif gender== "female":
	# 		x_female= 655.1+4.35*(weight)+4.7*(height)-4.7*(age)
	# 		answer = x_female

#x_female is the number of calories a female should consume
#return int(answer)
#need to fix error checking for male, in the case that gender is inputted incorrectly

	return print ("You should consume " + str(answer) + " calories daily.")


'''if __name__=="__main__":
print("This program will calculate the number of calories you should consume per day.")
print("Please note this calculator may not be accurate for infants and young children.")

gender= input("Are you male or female?>> ")

#while gender != "male" or gender != "female":
#gender= input("Error, please type in gender again")
#else:
weight= float(input("How much do you weigh in pounds?>> "))
height= float(input("How tall are you in inches?>> "))
age= float(input("How many years old are you?>> "))

final_answer = calorie_intake(gender, weight, height, age)

print ("You should consume " + str(final_answer) + " calories daily")'''
