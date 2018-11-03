#The lists of Monopoly and the dictionary of numbers
color = ['purple' , 'light blue' , 'maroon' , 'orange' , 'red' , 'yellow' , 'green' , 'dark blue']
size = [2, 3, 3, 3, 3, 3, 3, 2]
cost = [50, 50, 100, 100, 150, 150, 200, 200]
numbers = {0: 'zero' , 1: 'one' , 2: 'two' , 3: 'three' , 4: 'four' , 5: 'five' , 6: 'six' , 7: 'seven' , 8: 'eight' , 9: 'nine' , 10: 'ten'}

#Input the color choosed and the amount of money available (also change the type of money to integer)
choose_color = input('Which color block will you be building on? ')
amount_of_money = input('How much money do you have to spend? ')
amount_of_money = int(amount_of_money)

#Value of important variables in the corresponding lists
properties = size[color.index(choose_color)]
each_cost = cost[color.index(choose_color)]

#Compute the number of houses that can be built
house_build = amount_of_money // each_cost

#Compute the number of houses each property can build
house_less = house_build//properties
house_more = house_less + 1

#Compute the number of properties
properties_more = house_build % properties
properties_less = properties - properties_more

#Output the results
print('There are' , numbers[properties] , 'properties and each house costs' , each_cost)
print('You can build' , numbers[house_build] , 'house(s) --' , numbers[properties_less] , 'will have' , numbers[house_less] , 'and' , numbers[properties_more] , 'will have' , numbers[house_more])
