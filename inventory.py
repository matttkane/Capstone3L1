import math
from tabulate import tabulate

class Shoe():

    # Constructor created that initializes attributes of the objects in the class Shoe

    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
'''Method created that pulls the information for each object in the class 'Shoe' and displays
it in a readable format. The try/except/finally block prints a message if the file doesn't
exist and makes sure the rest of the code still runs even if the except block does not execute.
The for loop splits the data into individual elements and then creates a new object with the
information as attribues and appends the object to the empty list 'shoes'. The if statement
tells the program not to create an object with attributes from the first line, which contains
the headings Country, Code, Product, Cost, Quantity.'''

def read_data(shoes):

    try:
        file = open("inventory.txt", "r")

    except FileNotFoundError:
        print("File does not exist.")

    finally:
        lines = file.readlines()

        for line in lines:
            temp = line.split(",")       

            if "Country" not in temp:
                shoes.append(Shoe(temp[0], temp[1], temp[2], temp[3], temp[4]))

        for i in range(len(shoes)):
            print(f'''
Country: {shoes[i].country.strip()}
Code: {shoes[i].code.strip()}
Product: {shoes[i].product.strip()}
Cost: {shoes[i].cost.strip()}
Quantity: {shoes[i].quantity.strip()}
''')

    file.close()         

# Empty list created to which to add objects of 'Shoe' class

shoes = []


'''Method created that allows the user to enter a product code and then returns the name of
the product related to that code. The first for loop displays the list of products and codes
to the user. The input command is used to get the code the user wants to search for. Then the
for loop uses an if statement to find the product and then prints out the product name.'''

def searchForCode(shoes):

    print("Product codes:")
    
    for i in range(len(shoes)):
        print(f"{shoes[i].product.strip()} : {shoes[i].code.strip()}")

    code = input("Enter the code to search for: ")

    for j in range(len(shoes)):
        if code in shoes[j].code:
            print('\n' + shoes[j].product.strip())


'''Method created that finds the product with the lowest quantity and then allows the user to choose
an amount to restock it to. An empty list is created, and the for loops appends the quantity value of
each object in the 'shoes' list to the empty list 'quantities'. Then each item in the list is cast to
an integer and the min() function is used to find the lowest one. The if statement finds the object in
the list with the quantity that matches the lowest one. The product name and quantity are printed and
the user is asked whow much they would like to restock. Finally the quantity value of that object is
changed to the restock value and a success message is displayed.'''

def findLowest(shoes):

    quantities = []

    for i in range(len(shoes)):
        quantities.append(shoes[i].quantity)
    
    for i in range(len(quantities)):
        quantities[i] = int(quantities[i])

    lowest = min(quantities)
    
    for a in range(len(shoes)):       
        if str(lowest) == shoes[a].quantity.strip():

            print(f'''
The product with the lowest quantity is {shoes[a].product.strip()} with {shoes[a].quantity.strip()} units''')

            restock = input("How much of the item would you like to restock? ")
            shoes[a].quantity = restock

            print(f'''
Success. {shoes[a].product.strip()} has been restocked to {restock} units''')


'''Method created that finds the product with the highest quantity and then allows the user to choose a
sale price that they would like to mark it to. An empty list is created and then the for loop appends the
quantity attributes of the objects in the list 'shoes' to the empty list. The second for loop casts all
the elements in the list to integers and then max() is used to find the highest one. The next for loop
looks through the quantity attributes of the objects and the if statement executes when the quantity
macthes the highest quantity. The user is asked what price they would like to change the item to and then
the cost attribute of that object is changed to the user's choice.'''

def findHighest(shoes):

    quantities = []

    for i in range(len(shoes)):
        quantities.append(shoes[i].quantity)

    for i in range(len(quantities)):
        quantities[i] = int(quantities[i])

    highest = max(quantities)

    for a in range(len(shoes)): 
        if str(highest) == shoes[a].quantity.strip():
            
            print(f'''
The product with the highest quantity is {shoes[a].product.strip()} with {shoes[a].quantity.strip()} units''')

            salePrice = input("Enter the sale price for this item: ")
            shoes[a].cost = salePrice
            
            print(f'''
Success. {shoes[a].product.strip()} is now on sale for R{salePrice.strip()}''')


'''Method created that calculates the stock value of each object in the class by multiplying the cost and
quantity attributes together, and then adds a new column to the data and writes it back the file with the
new 'Value' column at the end. The file is opened with the mode set to read only, then the for loop loops
through the indexes of 'shoes' and stores the product of the cost and quantity attributes of each object
in a new variable called 'value'. The try/except block changes the variable 'value' simply to the string
'Value' if the product of the cost and quantity attributes returns a ValueError (i.e., it is the heading
line). 'value' for each object is cast into a string and then .append() is used to add an element to the
end of each line representing 'value'. Each element of each line is then written back to the file using an
fstring and indexing. Finally, each 'temp' is appended to the empty list created earlier called 'table',
creating a 2D list, and then the tabulate function is used to display a table out of the 2D list.'''

def value_per_item():

    file = open("inventory.txt", "r")
    lines = file.readlines()
    file.close()

    for i in range(len(shoes)):
        value = int(shoes[i].cost) * int(shoes[i].quantity)
        
    file = open('inventory.txt', 'r+')

    table = []

    for line in lines:
        temp = line.split(",")
        
        new = temp.pop(4)
        new = new.strip('\n')
        temp.append(new)

        try:
            value = int(temp[3]) * int(temp[4])

        except ValueError:
            value = "Value"

        value = str(value)        
        temp.append(value + "\n")      
        file.write(f"{temp[0]}, {temp[1]}, {temp[2]}, {temp[3]}, {temp[4]}, {temp[5]}") 
       
        table.append(temp)
    
    print(tabulate(table))

    file.close()

# Functions called with 'shoes' list as input

print("Shoe information:")

read_data(shoes)

userChoice = int(input('''What would you like to do?

1 - Search for a shoe by code
2 - Place shoe with highest stock on sale
3 - Restock shoe with lowest stock
4 - Display table of shoe information
5 - Quit

Selection: '''))

while userChoice != 5:

    if userChoice == 1:
        searchForCode(shoes)
    elif userChoice == 2:
        findHighest(shoes)
    elif userChoice == 3:
        findLowest(shoes)
    elif userChoice == 4:
        value_per_item()

    userChoice = int(input('''
    What would you like to do?

    1 - Search for a shoe by code
    2 - Place shoe with highest stock on sale
    3 - Restock shoe with lowest stock
    4 - Display table of shoe information
    5 - Quit

    Selection: '''))
