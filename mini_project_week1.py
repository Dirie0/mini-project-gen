
def productmenu():
    product = []
    while True:
        option = input("Please select from the following options:\nEnter (0) to return to main menu\nEnter (1) to show all products\nEnter (2) to add another product\n")
        if option ==  "0":
            mainmenu()
        elif option == "1":
            print(f'YOU HAVE ADDED THE FOLLOWING PRODUCTS: {product}')
            continue
        elif option == "2":
            product_choice = str(input("PLEASE ADD A PRODUCT: "))
            product.append(product_choice)
            continue
        else:
            print("YOU HAVE ENTERED THE WRONG OPTION, PLEASE TRY AGAIN")
            productmenu()
        return
    
def mainmenu():
    print("Welcome to the store!")
    print("Enter (0) to exit the app\nEnter (1) to enter product menu")
    choice = input()
    if choice == "0":
        print("THANKS FOR YOUR TIME, GOODBYE!")
        exit()
    elif choice == "1":
        productmenu()
    else:
        print("YOU HAVE ENTERED THE WRONG OPTION PLEASE TRY AGAIN")
        mainmenu()
mainmenu()
    
