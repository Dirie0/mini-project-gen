
file1 = open ("products_1.txt", 'r')

file2 = open("couriers_1.txt" , 'r')

orderdictionary={'Customer Name':'', 'Customer Address':'', 'Customer Phone':'', 'Courier':'', 'Order Status':''}
orderlist=[]
def ordersmenu():
    while True:
        order = input("Enter(0) to return to main menu\nEnter(1) to show all orders\nEnter(2) to enter order details\nEnter(3) to update existing order status to ready\n")
        if order == "0":
            mainmenu()
        elif order == "1":
              print(orderlist)
              continue 
        elif order == "2":        
            orderdictionary={'Customer Name':'', 'Customer Address':'', 'Customer Phone':'', 'Courier':'', 'Order Status':''}       
            file2 = open("couriers_1.txt", 'r')
            content = file2.read().splitlines() 
            enumrateContent= enumerate(content)
            print(list(enumrateContent))
            file2.close()
            customer_name = input("Please enter your full name:\n")
            customer_address = input("Please enter your address:\n")
            customer_phone = input("Please enter your phone number:\n")
            customer_courier_selection = input("Please enter a number from the list above that corresponds with a courier of your choice:\n")
            order_status = "PREPARING"
            orderdictionary["Customer Name"]= customer_name
            orderdictionary["Customer Address"]= customer_address
            orderdictionary["Customer Phone"]= customer_phone
            orderdictionary["Order Status"]= order_status
            orderdictionary['Courier']=customer_courier_selection
            orderlist.append(orderdictionary)
            print(f'You have added the following order{orderdictionary}')
            continue
        elif order == "3":
            print("Below is a list of the orders with indexed values")
            enumerateorderlist= enumerate(orderlist)
            print(list(enumerateorderlist))
            order_list_index = int(input("Please enter the number that corresponds with your chosen order:\n"))
            orderlist[order_list_index]["Order Status"]="READY"
            continue
        else:
            print("YOU HAVE ENTERED THE WRONG OPTION PLEASE TRY AGAIN")
            ordersmenu()
            return


def couriermenu():
    while True:
        courier_choice = input("Please select from the following options:\nEnter (0) to return to main menu\nEnter (1) to show all couriers\nEnter (2) to add a new courier\n")
        if courier_choice ==  "0":
            mainmenu()
        elif courier_choice == "1":
            file2 = open("couriers_1.txt", 'r')
            content = file2.read().splitlines() #same functionality as readlines but removes the \n at the end
            print(content)
            file2.close()
            continue
        elif courier_choice == "2":
            file2 = open("couriers_1.txt", "a") 
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
            file1 = open("products_1.txt", 'r')
            content = file1.read().splitlines() #same functionality as readlines but removes the \n at the end
            print(content)
            file1.close()
            continue
        elif product_choice == "2":
            file1 = open("products_1.txt", "a") 
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
    print("Enter (0) to exit the app\nEnter (1) to access the product menu\nEnter (2) to access the courier menu\nEnter (3) to access the order menu")
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
    elif choice == "3":
        ordersmenu()
    else:
        print("YOU HAVE ENTERED THE WRONG OPTION PLEASE TRY AGAIN")
        mainmenu()
mainmenu()
    

