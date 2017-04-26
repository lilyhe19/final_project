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
		if int(mainMenuInput) not in [1,2,3,4]: #error check if input is out of range
			mainMenuInput = input("Please type a number between 1 and 4: ")
		if mainMenuInput == 1: #call each separate method function
			pass
		if mainMenuInput == 2:
			import bmi
			bmi.BMI() #int(input("height(inches)>> ")),int(input("weight(pounds)>> ")))
			break
		if mainMenuInput == 3:
			pass
		if mainMenuInput == 4:
			pass
	return


if __name__ == "__main__":
	main()
	mainMenuReturn = input("\n Would you like to return to the main menu? (y/n)")
	if mainMenuReturn == 'y':
		main()
	if mainMenuReturn == 'n':
		print("Thanks for using EZHealth today!")
		#return
	else:
		 print ("Please enter either \"y\" or \"n\".")





	"""IGNORE THIS::::: I"M USING IT FROM MY OLD JAVA ASSIGNMENT"
	println("(C)reate mad-lib, (V)iew mad-lib, (Q)uit? "); #menu of three options
	do {
			System.out.println("(C)reate mad-lib, (V)iew mad-lib, (Q)uit? "); //menu of three options
			menuInput = console.next().toLowerCase(); //converts any letter to lower case

			//error checks if the user types a typo
			while (!(menuInput.startsWith("c")) && !(menuInput.startsWith("v")) && !(menuInput.startsWith("q"))) {
				System.out.println("(C)reate mad-lib, (V)iew mad-lib, (Q)uit? ");
				menuInput = console.next().toLowerCase(); //gives the user another chance to enter a menu option
			}

			if (!(menuInput.startsWith("q"))) { //user typed in C or V
				f = fileName(console); //returns a scanner that other methods can use

				if (menuInput.startsWith("c")) { //user wants to create

					fillIn(console, f, inputName);
				}else if (menuInput.startsWith("v")) { //user chooses "v"
						viewFile(console, f, inputName);
				}

			}

		} while (!(menuInput.startsWith("q"))); //program stops running when they press q to quit"""
