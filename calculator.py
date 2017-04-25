import math 
def calc(x): 
	"""given the radius as user input, returns the volume of the sphere
	
	examples here: 
	calc(5) = 523.5987755982989
	calc(0) = 0.0
	calc(11) = 5575.279762570686

	""" 
	volume = str((4/3)*math.pi*x**3); 
	return volume


if __name__ == "__main__": 
	print("This program tells you the volume of the sphere, given a certain radius")
	radius = int(input("Please enter a positive integer for the radius: "))

	answer = calc(radius)
	print("The volume of the sphere is " + answer) 