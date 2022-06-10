# Capstone3L1
Capstone Project 3 Level 1

This program creates a class of Shoe objects with the attributes country, code, product, cost and quantity, and a constructor that initializes the
attributes.

When the program begins, you are presented with a menu with choices to search for a shoe by code, place the shoe with the highest stock on sale, restock
the shoe with the lowest stock, or display a table with all the shoe information, as well as an option to exit. Depending on your choice, the correct
method is called to perform the required task.

If you choose to search for a shoe by code, you are presented with a list of the names of shoes as well as their corresponding codes. When you enter a
code, the product corresponding to that code is returned.

If you choose to place the shoe with the highest stock on sale, you are shown which shoe has the highest quantity and asked what you would like to change
the sale price to. The price attribute of the shoe in the list is then ammended to this price.

If you choose to restock the shoe with the lowest quantity, you are shown which shoe has the lowest quantity and then asked how much of the shoe you
would like to restock. The quantity attribute is then ammended to this value.

If you choose to display a table with all shoe information, the program displays a table with all the attribtes of the shoes. When calling this function,
the program also calculates the value of the stock of the shoe by finding the product of the price and quantity attributes, and adds a column onto the
end of the table containing the value of each shoe.
