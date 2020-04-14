answer = input("Is it raining?")
raining = (answer == "y")
if raining:
    answer = input("Is it windy?")
    windy = (answer == "y")
if raining and not windy:
    print("Take an umbrella.")
elif raining and windy:
    print("Take a raincoat.")
else: # not raining
    print("Enjoy your walk.")
