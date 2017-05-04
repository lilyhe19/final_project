def docs():
    '''
    Takes user input of location and returns the three doctors
    from nearest location (matching town/city).
    '''

    print("\n This program will find three doctors \
    \n from the locations nearest yours in Massachusetts \
    \n based on the location you input into this function.")

#convert CSV into a list of dictionaries
    import csv
    csv_file = csv.DictReader(open('DoctorSearch.csv'))
    input_city = input("Please type in the name of your city/town. (first letter uppercase, remaining letters in lowercase) \n ->  ")
    input_specialty = input("Please type in the name of the medical specialty you are looking for if this is applicable. \n If not, press Enter to continue. (first letter uppercase, remaining letters in lowercase; ie. Radiology, Oncology \n -> ")

    #TENTATIVE CODE
    # found = False #use boolean to error check

    # while found == False:
    #     for x in row['City']:
    #         if input_city != x:
    #             found = True
    #     input_city = input("Please try another city/town. \n ->")

    closest = [row for row in csv_file if row['City'] == input_city]

    if input_specialty != []:
        closest = [row for row in csv_file if row['City'] == input_city and row['Specialty' == input_specialty]
    elif input_specialty == []:
        closest = [row for row in csv_file if row['City'] == input_city]

    first = closest[0]
    second = closest[1]
    third = closest[2]

    return print("The three doctors nearest you are: \n 1.", first['\ufeffFirst Name'], first['Last Name'], "at", first['Hospital'],"who specializes in",second['Specialty'], "\
    \n 2.",second['\ufeffFirst Name'],second['Last Name'],"at",second['Hospital'],"who specializes in",second['Specialty'], "\
    \n 3.",third['\ufeffFirst Name'],third['Last Name'],"at",third['Hospital'],"who specializes in",second['Specialty'])



#if __name__ == "__main__":
#Intro
#Prompt
#
#Prints the answer
#    print("")
