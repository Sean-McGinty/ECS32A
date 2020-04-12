#moon.py
#ECS32A
#
#Converts an individual's weight on Earth to their weight on the moon
earth_weight=float(input("What is your weight on Earth?")) #Creates a variable for an individual's weight on Earth
moon_weight=str(earth_weight/6) #Converts their Earth weight to their Moon weight by dividing by 6
print("Your weight on the Moon is",moon_weight)
