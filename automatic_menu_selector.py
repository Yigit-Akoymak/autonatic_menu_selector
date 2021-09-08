#menu of the drinks and meals
drink_menu = ["coke","pepsi","ayran"]
meal = ["pizza","doner","lahmacun","kebap","chicken","salad"]
#Selecting process /meals
print("welcome to our restourant what would you like to eat")
print(meal)
meal_selection=(str(input(":>")))
#Selecting process /meals
print("what would you like to drink with" ,meal_selection)
print(drink_menu)
drink_selection=input(":>")
print("your",meal_selection ,"and",drink_selection, "will be ready in 30 minouts")
