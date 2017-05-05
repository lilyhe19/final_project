def docs():
    '''
    Takes user input of location and returns the three doctors
    from nearest location (matching town/city).
    '''

    print("\n This program will find three doctors \
    \n from the locations nearest yours in Massachusetts \
    \n based on the location you input into this function.")
    print("NOTE: This service is limited to only surrounding MA cities. More locations will be added soon. Thank you for your patience!")

#convert CSV into a list of dictionaries
    import csv
    csv_file = csv.DictReader(open('DoctorSearch.csv'))
    input_city = input("Please type in the name of your city/town. (first letter uppercase, remaining letters in lowercase) \n ->  ")
    #input_specialty = input("Please type in the name of the medical specialty you are looking for if this is applicable. \n If not, press Enter to continue. (first letter uppercase, remaining letters in lowercase; ie. Radiology, Oncology \n -> ")

    #TENTATIVE CODE
    # found = False #use boolean to error check

    # while found == False:
    #     for x in row['City']:
    #         if input_city != x:
    #             found = True
    #     input_city = input("Please try another city/town. \n ->")

    cities= [csv_file['City'] 

    if input_city not in cities:
        input_city = input("City unavailable, please type in another city.")

    #for x in cities:
        #if x != input_city:
            #input_city = input("City unavailable, please type in another city.")

    closest = [row for row in csv_file if row['City'] == input_city]

    first = closest[0]
    second = closest[1]
    third = closest[2]

    print("The three doctors nearest you are: \n 1.", first['First Name'], first['Last Name'], "at", first['Hospital'], "\
    \n 2.",second['First Name'],second['Last Name'],"at",second['Hospital'], "\
    \n 3.",third['First Name'],third['Last Name'],"at",third['Hospital'])




#if __name__ == "__main__":
#Intro
#Prompt
#
#Prints the answer
#    print("")
