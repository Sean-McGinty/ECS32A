#stim.py
#ECS32A
#
#Household Stimulus Check Calculation
number_adults=int(input("How many adults?")) #Creates a Variable for number of adults in a family
number_kids=int(input("How many kids?")) #Creates a variable for number of kids in a family
check_amount=str(500*number_kids+1200*number_adults) #Creates variable for the check amount to be recieved by the family
print("You will get a check for",check_amount,"dollars.")
