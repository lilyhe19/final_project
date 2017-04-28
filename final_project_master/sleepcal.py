def sleep(number):
    #tells you how much sleep you should get based on age
    #infants not included

    master= [{'age':[1,2],'hours':"11-14"},{'age':[3,4,5],'hours':"10-13"},{'age':[6,7,8,9,10,11,12,13],'hours':"9-11"},{'age':[14,15,16,17],'hours':"8-10"}]
    for x in master:
        if number in x['age']:
            return(x['hours'])  

if __name__ == "__main__":

    print("This program will tell you how many hours your child should sleep based on his/her age.")
    print("This program does apply to infants (children under one year old)")
    number = int(input("Please enter in an age (1-17 years): "))
    final_answer = sleep(number)
    print("Your child should sleep " + str(final_answer) + " hours.")
