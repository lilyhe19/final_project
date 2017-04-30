def docs():
    '''
    Takes user input of location and returns the three doctors from nearest location (matching town/city).
    '''

    print("\n This program will find three doctors \
    \n from the locations nearest yours in Massachusetts \
    \n based on the location you input into this function.")

#convert CSV into a list of dictionaries
    import csv
    csv_file = csv.DictReader(open('DoctorSearch.csv'))
    input_city = input("Please type in the name of your city/town. (first letter uppercase, remaining letters in lowercase) \n ->  ")

    closest = [row for row in csv_file if row['City'] == input_city]

    first = closest[0]
    second = closest[1]
    third = closest[2]

    return print("The three doctors nearest you are: \n 1.", first['\ufeffFirst Name'], first['Last Name'], "at", first['Hospital'], "\
    \n 2.",second['\ufeffFirst Name'],second['Last Name'],"at",second['Hospital'], "\
    \n 3.",third['\ufeffFirst Name'],third['Last Name'],"at",third['Hospital'])


#if __name__ == "__main__":
#Intro
#Prompt
#
#Prints the answer
#    print("")
