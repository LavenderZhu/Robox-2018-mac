#The lists of Monopoly
color = ['purple' , 'light blue' , 'maroon' , 'orange' , 'red' , 'yellow' , 'green' , 'dark blue']
size = [2, 3, 3, 3, 3, 3, 3, 2]
cost = [50, 50, 100, 100, 150, 150, 200, 200]

choose_color=''
#Allow the user to try again, until a suitable input is found. Blue is a special case~
while choose_color not in color:
    choose_color = input('Which color block will you be building on? ')
    if choose_color=='blue' : choose_color = input('light blue or dark blue? ')

#Input the amount of money available (also change the type of money to integer)
amount_of_money = input('How much money do you have to spend? ')
amount_of_money = int(amount_of_money)

#Value of important variables in the corresponding lists (and print them)
properties = size[color.index(choose_color)]
each_cost = cost[color.index(choose_color)]
print('There are' , properties , 'properties and each house costs' , each_cost)

#The situation that no building is affordable
if amount_of_money < each_cost :
    print('You cannot afford even one house.')

#Other situations
else :

    #Compute the number of houses that can be built
    house_build = amount_of_money // each_cost

    #Compute the number of houses each property can build
    house_less = house_build//properties
    house_more = house_less + 1
    
    #When the number of houses in each property is not all more than 4
    if house_less<=4 :
        properties_more = house_build % properties
        properties_less = properties - properties_more

        #omit 0's in the output
        if house_less==0 or properties_less==0 : print('You can build' , house_build , 'house(s) --' ,
                                                       properties_more , 'will have' , house_more)
        elif house_more==0 or properties_more==0 : print('You can build' , house_build , 'house(s) --' ,
                                                         properties_less , 'will have' , house_less)
        elif house_more==5 : print('You can build' , house_build , 'house(s) --' , properties_less , 'will have' ,
                                   house_less , 'and' , properties_more , 'will have a hotel')
        else :
            print('You can build' , house_build , 'house(s) --' , properties_less , 'will have' ,
                  house_less , 'and' , properties_more , 'will have' , house_more)
            
    #When the number of houses in each property is more than 4
    else :
        print('You can build' , house_build , 'house(s) --' , properties , 'will have a hotel')
