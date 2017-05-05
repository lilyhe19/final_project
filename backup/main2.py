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
		\n 6. Weight Based Divided Dose Calculator \
		\n 7. Forum")

	print("\n Type \"0\" to quit")

	mainMenuInput = int(input("\n Please type the number of the option you'd like to explore: "))

	while int(mainMenuInput) != 0:
		if int(mainMenuInput) not in [1,2,3,4,5,6,7]: #error check if input is out of range
			mainMenuInput = input("Please type a number between 1 and 4: ")

		elif mainMenuInput == 1: #call each separate method function
			pass

		elif mainMenuInput == 2:
			import bmi #imports function, if you change the name here, change it catch_error also
			bmi.BMI()
			import catch_error
			catch_error.error(2)
			break

		elif mainMenuInput == 3:
			import calcounter_alt
			calcounter_alt.calorie_intake()
			import catch_error
			catch_error.error(3)
			break

		elif mainMenuInput == 4:
			pass

		elif mainMenuInput == 5:
			import sleepcal_alt
			sleepcal_alt.sleep()
			import catch_error
			catch_error.error(5)
			break

		elif mainMenuInput == 6:
			pass

		elif mainMenuInput == 7:
			pass
	return


if __name__ == "__main__":
	main()
	mainMenuReturn = input("\n Would you like to return to the main menu? (y/n)  ")
	while True:
		if mainMenuReturn == 'y':
			main()
			mainMenuReturn = ""
			mainMenuReturn= input("\n Would you like to return to the main menu? (y/n)  ")
		elif mainMenuReturn == 'n':
			print("Thanks for using EZHealth today!")
			break
		else: #if types in wrong
		 	mainMenuReturn = input("Please enter either \"y\" or \"n\".")
		 #problem here where, on second time, it skips to this line bc of the else statement
