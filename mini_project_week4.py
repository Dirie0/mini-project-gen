
# orderdictionary={'Customer Name':'', 'Customer Address':'', 'Customer Phone':'', 'Courier':'', 'Order Status':''}
# orderlist=[]
# statuslist=[]
# def ordersmenu():
#     while True:
#         order = input("Enter(0) to return to main menu\nEnter(1) to show all orders\nEnter(2) to enter order details\nEnter(3) to update existing order status to ready\n")
#         if order == "0":
#             mainmenu()
#         elif order == "1":
#               print(orderlist)
#               continue 
#         elif order == "2":        
#             orderdictionary={'Customer Name':'', 'Customer Address':'', 'Customer Phone':'', 'Courier':'', 'Order Status':''}       
#             file2 = open("couriers_1.txt", 'r')
#             content = file2.read().splitlines() 
#             enumrateContent= enumerate(content)
#             print(list(enumrateContent))
#             file2.close()
#             customer_name = input("Please enter your full name:\n")
#             customer_address = input("Please enter your address:\n")
#             customer_phone = input("Please enter your phone number:\n")
#             customer_courier_selection = input("Please enter a number from the list above that corresponds with a courier of your choice:\n")
#             order_status = "PREPARING"
#             orderdictionary["Customer Name"]= customer_name
#             orderdictionary["Customer Address"]= customer_address
#             orderdictionary["Customer Phone"]= customer_phone
#             orderdictionary["Order Status"]= order_status
#             orderdictionary['Courier']=customer_courier_selection
#             orderlist.append(orderdictionary)
#             statuslist.append(order_status)
#             print(f'You have added the following order{orderdictionary}')
#             continue
#         elif order == "3":
#             print("Below is a list of the orders with indexed values")
#             enumerateorderlist= enumerate(orderlist)
#             print(list(enumerateorderlist))
#             order_list_index = int(input("Please enter the number that corresponds with your chosen order:\n"))
#             enumeratestatuslist= enumerate(statuslist)
#             print(list(enumeratestatuslist))
#             status_list_index = int(input("Please enter the number that corresponds with the order status you wish to update to ready:\n"))
#             # change status in status list and change status in order 
#             if status_list_index == order_list_index:
#                 statuslist[status_list_index]= "READY"
#                 orderlist[order_list_index]["Order Status"]="READY"
#             continue
#         else:
#             print("YOU HAVE ENTERED THE WRONG OPTION PLEASE TRY AGAIN")
#             ordersmenu()
#             return


# def couriermenu():
#     while True:
#         courier_choice = input("Please select from the following options:\nEnter (0) to return to main menu\nEnter (1) to show all couriers\nEnter (2) to add a new courier\n")
#         if courier_choice ==  "0":
#             print("return to main menu")
#         elif courier_choice == "1":
            
#             continue
#         elif courier_choice == "2":
            
#             continue
#         else:
#             print("YOU HAVE ENTERED THE WRONG OPTION, PLEASE TRY AGAIN")
#             print("call courier menu")
#         return


import csv
productdictionary = {"Product name": "", "Product price": "" }
productlist=[]
def productmenu(data):
    while True:
        product_choice = input("Please select from the following options:\nEnter (0) to return to main menu\nEnter (1) to show all products\nEnter (2) to add a new product\n")
        if product_choice ==  "0":
            print("call main menu")
        elif product_choice == "1":
            print(productlist)
            continue
        elif product_choice == "2":
            productdictionary= {"Product name": "", "Product price": "" }
            file1 = open("products.csv", "r")
            product_name = str(input("PLEASE ADD A PRODUCT NAME: "))
            product_price = float(input("PlEASE ADD THE PRODUCT PRICE: "))
            productdictionary["Product name"]=product_name
            productdictionary["Product price"]=product_price
            productlist.append(productdictionary)
            

            file1.write(str(productdictionary))
            file1.close()
            continue
        else:
            print("YOU HAVE ENTERED THE WRONG OPTION, PLEASE TRY AGAIN")
            productmenu()
        return
data = [1,2]
productmenu(data)

# Write the file
def write_file(filename):
    with open(filename) as file:
        print(file)

# Get's the filename  pathway
def get_filname():
    answer = input('filname?')
    return answer

user_ans = get_filname()

write_file(user_ans)

# def mainmenu():
#     print("Welcome to the store!")
#     print("Enter (0) to exit the app\nEnter (1) to access the product menu\nEnter (2) to access the courier menu\nEnter (3) to access the order menu")
#     choice = input()
#     if choice == "0":
#         print("THANKS FOR YOUR TIME, GOODBYE!")
#         file0= open("products.csv")
#         file0.close()
#         file1= open("orders.csv")
#         file1.close()
#         file2=open("couriers.csv")
#         file2.close()
#         exit()
#     elif choice == "1":
#         productmenu()
#     elif choice == "2":
#         couriermenu()
#     elif choice == "3":
#         ordersmenu()
#     else:
#         print("YOU HAVE ENTERED THE WRONG OPTION PLEASE TRY AGAIN")
#         mainmenu()
# mainmenu()
    

