#/***************
# Avraham sikirov
# 318731478
# 01
# ass7
#***************/

from collections import defaultdict
import sys

"""
* Function Name: is_product_exists
* Input: main dict and category.
* Output: False if product doesn't exists, and the category it self if exists.
* Function Operation: The function goes through the entire dictionary
* and checks if the inserted category exists within
* it and if so it returns the category of the product.
"""

def is_product_exists(categories, product):
    flag = False 
    temp = 1
    for i in categories:
         for j in categories[i]:
             if (product == j):
                 flag = i
    if (flag == False):
        return False
    else:
        return flag

"""
* Function Name: is_category_exists
* Input: main dict and category to check
* Output: False if category doesn't exists, and the category it self if exists.
* Function Operation: The function goes through the entire
* dictionary and checks if the inserted category
* exists within it and if so it returns the category.
"""

def is_category_exists(categories, category):
    if categories != None:
        for i in categories:
            if category == i:
                return True
    return False

"""
* Function Name: save_product
* Input: main dict
* Output: dict to file
* Function Operation:First the function sorts the whole dictionary,
* then goes through each category and all its products
* and chains it into a variable and finally puts everything into the file
"""


def save_product(categories):
    f = open(output_to, "w")
    if (categories != None):  
        # sorting the categories in the main dict
        categories = {k: v for k, v in sorted(categories.items())}
        for i in categories:
            # sorting the products in the sub dict.
            categories[i] = {k: v for k, v in sorted(categories[i].items())}
        for i in categories:
            str_w = str(i) + ":"
            for j in categories[i]:
                # chain the categories the "str_w"
                str_w = str_w + str(j) + "," + str(categories[i][j]) + ";"
            str_w = str_w + '\n'
            f.write(str_w)
    else:
        f.write("")
    print("Store saved to", '"' + output_to + '"' + ".")
    f.close()
    return

"""
* Function Name: add_product
* Input: main dict
* Output: new dict
* Function Operation: First the function checks the correctness of the 
* input so that there is enough information, 
* that the categories exist and the price is correct. 
* The function then puts the new product and its price in the appropriate 
* categories in the dictionary and in addition deletes the relevant values ​​from the cache

"""

def add_product(categories, cache):
    temp = input()
    # check that there is minumum data required  (category and products)
    if (temp.count(',') < 1 or temp.count(':') < 1):
        print("Error: not enough data.")
        return categories, cache
    user_input = temp.split(':')
    categories_input = user_input[0].lstrip()
    product_input = user_input[1].lstrip()
    admin_categories = categories_input.split(",")
    # check that there is minumum data required  (product and price)
    if (product_input.count(',') < 1):
        print("Error: not enough data.")
        return categories, cache
    admin_product, admin_price = product_input.split(",", 1)
    # check that all the categories exists
    for i in admin_categories:
        if (is_category_exists(categories, i.lstrip()) == False):
            print("Error: one of the categories does not exist.")
            return categories, cache
    # check that that price is positive integer
    if(admin_price.lstrip().isnumeric() != True or int(admin_price.lstrip()) < 0 ):
        print("Error: price is not a positive integer.")
        return categories, cache
    # goes over the the input categories and inserting the new values to the dict.
    for i in admin_categories:
        categories[i.lstrip()][admin_product.lstrip()] = admin_price.lstrip()
    print("Item", '"' + admin_product.lstrip() + '"', "added.")
    cache = dict()
    return categories, cache

"""
* Function Name: admin_panel
* Input: main dict
* Output: new dict (if changed)
* Function Operation:First the function checks that the password 
* from the user matches the password in the file
* Then with the help of a loop the function requests 
* input for action from the user and calls the appropriate function
"""

def admin_panel(categories, cache):
    print("Password: ", end = "")
    password = input()
    f = open(admin_file, 'r')
    f.close
    # check if the password are matched.
    if (password != f.read().lstrip()):
        print("Error: incorrect password, returning to main menu.")
        return categories, cache
    # sub menu for the admin. 
    ans = True
    while (ans != 0):
        print_sub_menu()
        ans=input()
        if ans=="1": 
        # assign to the main dict the dict with the added product.
         categories, cache = add_product(categories, cache) 
        elif ans=="2":
          save_product(categories)
        elif ans =="0":
          return categories, cache
        else:
          print("Error: unrecognized operation.")
          continue

"""
* Function Name: purchase_an_item
* Input: main dict
* Output: Updated dict.
* Function Operation: First the function announces a new dictionary 
* and checks in which categories the product is located. 
* The function then copies the old dictionary to 
* the new one without the purchased product 
* In addition the function deletes the relevant data for that product from the cache
"""

def purchase_an_item(categories, cache):
    temp = input()
    temp = temp.lstrip()
    temp_dict1 = {}
    # check in which categories the product exists. 
    which_category = is_product_exists(categories, temp)
    # if no category found the function will print en error and will return the same dict.
    if (which_category == False):
         print("Error: no such item exists.")
         return categories, cache
     # copy the old dict to the new one without the purchesed product. 
    for i in categories:
         temp_dict2 = {}
         for j in categories[i]:
             if (temp == j):
               price = categories[i][j]
               continue
             temp_dict2[j] = categories[i][j]
         temp_dict1[i] = temp_dict2
    print("You bought a brand new", '"' + temp + '"', "for",price + "$.")
    # delete from the cash the values associated with this product. 
    cache = dict()
    # return the new dict to be the main dict. 
    return temp_dict1, cache

"""
* Function Name: query_by_item
* Input: main dict
* Output: print the group of items. 
* Function Operation: First the function checks that the product
* exists and if it exists checks if it already has the
* information about it in the cache, if not the function goes
* through the entire dictionary and puts the relevant
* products in the list that is sorted and printed
"""
                      
def query_by_item(categories, cache):
     temp = input()
     temp = temp.lstrip()
     
     temp_list = set()
     # check if the products exists. 
     if (is_product_exists(categories, temp) == False):
         print("Error: no such item exists.")
         return
     # check if data already exists in cache. 
     if temp in cache.keys():
         print("Cached:", cache[temp])
         return
     # goes over the dict and add the product to the list
     for i in categories:
         for j in categories[i]:
             if (temp == j):
                 for k in categories[i]:
                    temp_list.add(k)
     temp_list.remove(temp)
     # add the data from the list to the cache. 
     cache[temp] = sorted(temp_list)
     print(sorted(temp_list))

"""
* Function Name: compare_dict
* Input: main dict, two prodcuts and an operator.
* Output: Prints the comparrison between the categories as asked.
* Function Operation: First the function transmits the
* information to a set type then checks which 
* comparison the user wants, performs the
* comparison and prints its results and save them in the cache dict. 
"""

def compare_dict(first_product, second_product, operator, products, cache):
    temp_list_1 = set()
    temp_list_2 = set()
    temp_tuple = first_product,second_product,operator
    # move the data to set. 
    for i in products[first_product]:
            temp_list_1.add(i)
    for j in products[second_product]:  
            temp_list_2.add(j)
    # check which operation is needed
    if (operator == '&'):
        process = sorted(list(temp_list_2.intersection(temp_list_1)))
        print(process)
        # save the result in the cache dict.
        cache[temp_tuple] = process 
    elif (operator == '|'):
         process = sorted(list(temp_list_2.union(temp_list_1)))
         print(process)
         # save the result in the cache dict.
         cache[temp_tuple] = process 
    elif (operator == '^'):
       process = sorted(list(temp_list_2.symmetric_difference(temp_list_1)))
       print(process)
       # save the result in the cache dict.
       cache[temp_tuple] = process
    else:
        print("Error: unsupported query operation.")
        return

"""
* Function Name: query_by_category
* Input: main dict
* Output:
* Function Operation: First the function performs normal
* tests for the input, tests that make
* sure that there is enough information and that it is correct and binding.
* Then if the action is stored in the cache they are printed,
* if not the function calls an auxiliary function that will perform the comparison
"""

def query_by_category(products, cache):
    flag1 = 0
    flag2 = 0
    temp = input()
    # check that there is enough commas.
    if (temp.count(',') < 2):
        print("Error: not enough data.")
        return
    user_input = temp.split(',', NUMBER_OF_SPLITS)
    first_product = user_input[0].lstrip()
    second_product = user_input[1].lstrip()
    operator = user_input[2].lstrip()
    # check that there is data between every comma 
    if (len(first_product) < MIN_LEN or len(second_product) < MIN_LEN or len(operator) < MIN_LEN):
        print("Error: not enough data.")
        return
    if products != None:
    #check that the cartegories exists in the dict.
        for i in products:
            if (i == first_product):
                flag1 = 1
            if (i == second_product):
                flag2 = 1
        if (flag1 == 0 or flag2 == 0):
            print("Error: one of the categories does not exist.")
            return
        # check that the operator is correct. 
    if temp[-1:] != '&' and temp[-1:] != '|' and temp[-1:] != '^' or len(operator) > MAX_LEN:
        print("Error: unsupported query operation.")
        return
    first_tuple = first_product,second_product,operator 
    second_tuple = second_product,first_product,operator
    # check if the first order is in the cache if so, print the value from the cash
    if (first_tuple) in cache.keys():
        print("Cached:", cache[first_product,second_product,operator])
        return
     # check if the second order is in the cache if so, print the value from the cash
    if (second_tuple) in cache.keys():
        print("Cached:", cache[second_product,first_product,operator])
        return
    # if not cashed the function calls this function to make the comparison operations. 
    compare_dict(first_product, second_product, operator,products, cache)

"""
* Function Name: create_dict
* Input:
* Output: full dict
* Function Operation: The function goes over a file with categories 
* and products and enters the categories to main dict and every product and it's price
* to sub dict.
"""

def create_dict():
    categories = {}
    f = open(store_file, 'r')
    for line in f:
        if (line == '\n'):
            continue
        line = line.lstrip()
        # split to the category and all the products. 
        token = line.split(':')
        cateogry_name = token[0].lstrip()
        # split to couple - product and price
        couple = token[1].split(';')
        products = {}
        for element in couple:
            # if there is no products in the category
            if element == "" or element == "\n":
                categories[cateogry_name] = products
                continue
            if(len(element) < 1 or element == "\n"):
                continue
            product_name,product_price = element.split(',')
            # insert the products and price to the sub dict.
            products[product_name.lstrip()] = product_price.lstrip()
            # insert the sub dict to the main dict by category
            categories[cateogry_name] = products
    f.close() 
    return categories

"""
* Function Name: Print_menu
* Input:
* Output: Sub menu
* Function Operation: Prints the sub menu
"""

def print_menu():
    print("Please select an operation:")
    print("\t0. Exit.")
    print("\t1. Query by category.")
    print("\t2. Query by item.")
    print("\t3. Purchase an item.")
    print("\t4. Admin panel.")

"""
* Function Name: print_sub_menu
* Input:
* Output: Sub menu
* Function Operation: Just prints the sub menu
"""

def print_sub_menu():
    print("Admin panel:")
    print("\t0. Return to main menu.")
    print("\t1. Insert or update an item.")
    print("\t2. Save.")

"""
* Function Name: main
* Input:
* Output: print: Error: unrecognized operation. if entered wrong key
* Function Operation: calls the function which creates the main dict. 
* and then there is a infinite loop for menu until the user enters '0'
"""

def main():
    categories = {}
    cache = dict()
    categories = create_dict()
    ans = True
    while (ans != 0):
        print_menu()
        ans=input()
        if ans=="1": 
          query_by_category(categories, cache)
        elif ans=="2":
          query_by_item(categories, cache)
        elif ans=="3":
          categories, cache = purchase_an_item(categories, cache)
        elif ans=="4":
          categories, cache = admin_panel(categories, cache) 
        elif ans =="0":
          return
        else:
          print("Error: unrecognized operation.")

if __name__ == "__main__":
    NUMBER_OF_SPLITS = 2
    MIN_LEN = 1
    MAX_LEN = 1
    dict_changed = False
    store_file = sys.argv[1]
    admin_file = sys.argv[2]
    output_to = sys.argv[3]
    #store_file = "store.txt"
    #admin_file = "admin.txt"
    #output_to = "out.txt"
    main()