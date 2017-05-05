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

    input_city = input("Please type in the name of your city/town. (first letter uppercase, remaining letters in lowercase):  ")


    cities= [row['City'] for row in csv_file]


    while input_city not in cities:
        input_city = input("City unavailable, please type in another city:  ")


    csv_file2 = csv.DictReader(open('DoctorSearch.csv'))
    closest = [row for row in csv_file2 if row['City'] == input_city]


    first = closest[0]
    second = closest[1]
    third = closest[2]

    print("Three doctors near you are: \n 1.", first['First Name'], first['Last Name'], "at", first['Hospital'], "\
    \n 2.",second['First Name'],second['Last Name'],"at",second['Hospital'], "\
    \n 3.",third['First Name'],third['Last Name'],"at",third['Hospital'])
