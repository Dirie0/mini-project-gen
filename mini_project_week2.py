#load

# file1 = open ("products.txt", 'r')

# file2 = open("couriers.txt" , 'r')

# def couriermenu():
#     while True:
#         courier_choice = input("Please select from the following options:\nEnter (0) to return to main menu\nEnter (1) to show all couriers\nEnter (2) to add a new courier\n")
#         if courier_choice ==  "0":
#             mainmenu()
#         elif courier_choice == "1":
#             file2 = open("couriers.txt", 'r')
#             content = file2.read().splitlines() #same functionality as readlines but removes the \n at the end
#             print(content)
#             file2.close()
#             continue
#         elif courier_choice == "2":
#             file2 = open("couriers.txt", "a") 
#             courier_choice = str(input("PLEASE ADD A COURIER: "))
#             file2.write(courier_choice + '\n')
#             file2.close()
#             continue
#         else:
#             print("YOU HAVE ENTERED THE WRONG OPTION, PLEASE TRY AGAIN")
#             productmenu()
#         return

# def productmenu():
#     while True:
#         product_choice = input("Please select from the following options:\nEnter (0) to return to main menu\nEnter (1) to show all products\nEnter (2) to add a new product\n")
#         if product_choice ==  "0":
#             mainmenu()
#         elif product_choice == "1":
#             file1 = open("products.txt", 'r')
#             content = file1.read().splitlines() #same functionality as readlines but removes the \n at the end
#             print(content)
#             file1.close()
#             continue
#         elif product_choice == "2":
#             file1 = open("products.txt", "a") 
#             product_choice = str(input("PLEASE ADD A PRODUCT: "))
#             file1.write(product_choice + '\n')
#             file1.close()
#             continue
#         else:
#             print("YOU HAVE ENTERED THE WRONG OPTION, PLEASE TRY AGAIN")
#             productmenu()
#         return

# def mainmenu():
#     print("Welcome to the store!")
#     print("Enter (0) to exit the app\nEnter (1) to access the product menu\nEnter (2) to access the courier menu")
#     choice = input()
#     if choice == "0":
#         print("THANKS FOR YOUR TIME, GOODBYE!")
#         file1.close()
#         file2.close()
#         exit()
#     elif choice == "1":
#         productmenu()
#     elif choice == "2":
#         couriermenu()
#     else:
#         print("YOU HAVE ENTERED THE WRONG OPTION PLEASE TRY AGAIN")
#         mainmenu()
# mainmenu()


file1 = open ("products.txt", 'r')

file2 = open("couriers.txt" , 'r')

def couriermenu():
    while True:
        courier_choice = input("Please select from the following options:\nEnter (0) to return to main menu\nEnter (1) to show all couriers\nEnter (2) to add a new courier\n")
        if courier_choice ==  "0":
            mainmenu()
        elif courier_choice == "1":
            file2 = open("couriers.txt", 'r')
            content = file2.read().splitlines() #same functionality as readlines but removes the \n at the end
            print(content)
            file2.close()
            continue
        elif courier_choice == "2":
            file2 = open("couriers.txt", "a") 
            courier_choice = str(input("PLEASE ADD A COURIER: "))
            file2.write(courier_choice + '\n')
            file2.close()
            continue
        else:
            print("YOU HAVE ENTERED THE WRONG OPTION, PLEASE TRY AGAIN")
            productmenu()
        return

def productmenu():
    while True:
        product_choice = input("Please select from the following options:\nEnter (0) to return to main menu\nEnter (1) to show all products\nEnter (2) to add a new product\n")
        if product_choice ==  "0":
            mainmenu()
        elif product_choice == "1":
            file1 = open("products.txt", 'r')
            content = file1.read().splitlines() #same functionality as readlines but removes the \n at the end
            print(content)
            file1.close()
            continue
        elif product_choice == "2":
            file1 = open("products.txt", "a") 
            product_choice = str(input("PLEASE ADD A PRODUCT: "))
            file1.write(product_choice + '\n')
            file1.close()
            continue
        else:
            print("YOU HAVE ENTERED THE WRONG OPTION, PLEASE TRY AGAIN")
            productmenu()
        return

def mainmenu():
    print("Welcome to the store!")
    print("Enter (0) to exit the app\nEnter (1) to access the product menu\nEnter (2) to access the courier menu")
    choice = input()
    if choice == "0":
        print("THANKS FOR YOUR TIME, GOODBYE!")
        file1.close()
        file2.close()
        exit()
    elif choice == "1":
        productmenu()
    elif choice == "2":
        couriermenu()
    else:
        print("YOU HAVE ENTERED THE WRONG OPTION PLEASE TRY AGAIN")
        mainmenu()
mainmenu()
    


