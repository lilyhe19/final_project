#import math

def main():
	"""
	docstring
	"""
	print("Welcome to EZHealth \n \n Here are your options:")
	print("\
		\n 1. Look up a doctor by location \
		\n 2. Calculate your BMI \
		\n 3. Calculate the number of calories you should consume for your age and weight\
		\n 4. Access the recommended baby items checklist to be prepared for almost any situation \
		\n 5. Sleep Calculator \
		\n 6. Weight Based Divided Dose Calculator")
	print("\n Type \"0\" to quit")

	mainMenuInput = int(input("\n Please type the number of the option you'd like to explore: "))

	while int(mainMenuInput) != 0:
		if int(mainMenuInput) not in [1,2,3,4, 5,6]: #error check if input is out of range
			mainMenuInput = input("Please type a number between 1 and 4: ")
		elif mainMenuInput == 1: #call each separate method function
			pass
		elif mainMenuInput == 2:
			import bmi #imports
			bmi.BMI() #int(input("height(inches)>> ")),int(input("weight(pounds)>> ")))
			break
		elif mainMenuInput == 3:
			import calcounter
			calcounter.calorie_intake()
			break
		elif mainMenuInput == 4:
			pass
		elif mainMenuInput == 5:
			pass
		elif mainMenuInput == 6:
			pass
	return


if __name__ == "__main__":
	main()
	mainMenuReturn = input("\n Would you like to return to the main menu? (y/n)")
	while mainMenuReturn == "y" or mainMenuReturn == "n":
		if mainMenuReturn == 'y':
			main()
			mainMenuReturn = ""
			mainMenuReturn= input("\n Would you like to return to the main menu? (y/n)")
		if mainMenuReturn == 'n':
			print("Thanks for using EZHealth today!")
		#return
	else: #if types in wrong
		 mainMenuReturn = input("Please enter either \"y\" or \"n\".")
		 #problem here where, on second time, it skips to this line bc of the else statement
