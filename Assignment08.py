# ------------------------------------------------------------------------------------------------ #
# Title: Assignment 8
# Description: Working with Classes
# ChangeLog (Who,When,What):
#                           RRoot, 1.1.2030, Created started script
#                           RRoot, 1.1.2030, Added pseudo-code to start assignment 8
#                           RHiatt, 3.7.2021, Added code and modified code to complete assignment
# ------------------------------------------------------------------------------------------------ #

# Data ------------------------------------------------------------------------------------------- #

import pickle

file_name = "Products.dat"
list_of_product_objects = []

class Product(object):
    """Stores data about a product:
    properties:
        product_name: (string) with the product  name
        product_price: (float) with the product standard price
    methods:
    changelog: (When, Who, What)
        RRoot, 1.1.2030, Created Class
        RHiatt, 3.7.2021, Modified code to complete assignment 8
    """

    str_Product = ""
    flt_Price = 0

    def __init__(self, product= '', price = 0):
        self.str_Product = product
        self.flt_Price = price

    @property # @property is a built-in decorator
    def product_name(self):
        return str(self.product_name)

    @property
    def product_price(self):
        return float(self.product_price)

# Data ------------------------------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------------------------------ #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:
    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        RHiatt, 3.7.2021, Added code
    """

    @staticmethod
    def read_data_from_file(file_name, list_of_product_objects):
        try:
            file = open(file_name, "rb")
            lst_pickle = lst_pickle.load(file)
            list_of_product_objects += lst_pickle
            file.close()
        except:
            print("No file found.")

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """Writes data to a binary file"""
        file = open(file_name, "wb")
        p = pickle.dump(list_of_product_objects, file)
        file.close()

# Processing  ------------------------------------------------------------------------------------ #

# Presentation (Input/Output)  ------------------------------------------------------------------- #
class IO:
    @staticmethod
    def print_menu_tasks():
        """display menu of choices"""
        print(
            '''
           Welcome to the Home Inventory System! \n
           Choose one of the following menu options... \n
           1) Show Current Data
           2) Add More Entries
           3) Save and Exit
           ''')
        return
        print()

    @staticmethod
    def menu_choice():
        """ Gets the menu choice from a user"""
        choice = str(input("Enter menu option (1 - 3): "))
        return choice

    @staticmethod
    def get_product_data():
        """"get product data from user"""
        print()
        product = str(input("Enter Product: "))
        value = float(input("Enter Price: "))
        new_row = [product, value]
        list_of_product_objects.append(new_row)

    @staticmethod
    def print_inventory(list_of_product_objects):
        try:
            for row in list_of_product_objects:
                print(row)
        except:
            print("No object found.")
        return "\n"

# Presentation (Input/Output)  ------------------------------------------------------------------- #

# Main Body of Script  --------------------------------------------------------------------------- #

FileProcessor.read_data_from_file(file_name, list_of_product_objects)

print()
print("Current Inventory: ")

IO.print_inventory(list_of_product_objects)

# Show user menu of options / Get user's choice ------------------------------------------------- #

while True:
    IO.print_menu_tasks()
    user_choice = IO.menu_choice()
    if user_choice.strip() == '1':
        """Show user current data in the list of product objects"""
        print()
        print("Here's what we have so far...")
        print()
        IO.print_inventory(list_of_product_objects)
        continue

# Allow user to enter data ------------------------------------------------- #

    elif user_choice.strip() == '2':
        IO.get_product_data()
        print()
        print("Here's what we have so far...")
        print()
        IO.print_inventory(list_of_product_objects)
        continue

    elif user_choice.strip() == '3':
        print()
        print("Saving data and exiting the program...")
        print()
        FileProcessor.save_data_to_file(file_name, list_of_product_objects)
        print("Thanks for your time today. Take care!")
        break