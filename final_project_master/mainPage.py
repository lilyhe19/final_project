#import math

#def main_function(x): #input is the number chosen by user
#		"""
#		docstring
#		"""
#	return [1,2,3]
	#if 1: run the doctor csv
	#if 2: run BMI calc
	#etc. etc. etc h
	#pseudocode
	#pseudocode
	#put something here


	#return function


if __name__ == "__main__":
	print("Welcome to EZHealth \n \n Here are your options:")
	print("\
		\n 1. Look up a doctor by location \
		\n 2. Calculate your BMI \
		\n 3. Calculate the number of calories you should consume \
		\n 4. Access the recommended items checklist")
	print("\n Type \"0\" to quit")
	mainMenuInput = int(input("\n Please type the number of the option you'd like to explore: "))

	while mainMenuInput != 0: #0 is quit
		if mainMenuInput == 1:
			pass
		if mainMenuInput == 2:
			import bmi
			bmi.BMI() #int(input("height(inches)>> ")),int(input("weight(pounds)>> ")))
			#f = open(os.path.join(__location__, bmi.py))
			#from final-project-master2 import bmi
		if mainMenuInput == 3:
			pass
		if mainMenuInput == 4:
			pass
			#call each separate method function
		if int(mainMenuInput) not in [1,2,3,4]:
			mainMenuInput = int(input("Please type a number between 1 and 4: ")) #error check if input is out of range



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

	#print some instructions

	#answer = function
