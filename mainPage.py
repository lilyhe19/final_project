#import math 
#def main function(x): 
	#pseudocode 
	#pseudocode
	#put something here 

	#return function


if __name__ == "__main__": 
	print("Welcome to this Health App ")
	print("Here are your options:")
	print("1. Look up a doctor by location")
	print("2. Calculate your BMI")
	print("3. Calculate the number of calories you should consume")
	print("4. Print out a checklist of useful items")
	print("Type \"0\" to quit")
	mainMenuInput = int(input("Please type the number that you'd like: "))

	while mainMenuInput != 0: 
		if 1 <= mainMenuInput <= 4: 
			#call each separate method function 
		else: 
			mainMenuInput = int(input("Please type a number between 1 and 4: "))



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
