import csv 


def ordersmenu():
    while True:
        order = input("Enter(0) to return to main menu\nEnter(1) to show all orders\nEnter(2) to enter order details\nEnter(3) to update existing order status to ready\n") 

        if order == "0":
            mainmenu()


        
        elif order == "1":
            with open("orders.csv", mode= 'r') as file2:                
                 csv_file2 = csv.DictReader(file2)
                 for row in csv_file2:
                     print(row)
            continue
    

        elif order == "2":
            customer_name = input("Please enter your name: ") 
            customer_address = input("Please enter your address: ")
            customer_phone_number= int(input("Please enter your phone number: "))
            with open("products.csv", mode = 'r') as file:
                csv_file = csv.DictReader(file)               
                enumerating = enumerate(csv_file)
                readingproductlist= list(enumerating)       #reading enumerated orders csv file into list of enumerated order dictionaries for user
                print(readingproductlist)
            product_index_choice= str(input("Enter comma seperated numbers that corresponds with your chosen products(eg 1,2): "))
            numbers_list = product_index_choice.split(",")
            intergers = []
            for i in numbers_list:
                intergers.append(int(i))              #converting ("1,2") string into a list of [1,2] to append showing products added to the order
            print("list: ", intergers)
            with open("couriers.csv", mode = 'r') as file1:
                csv_file1 = csv.DictReader(file1)
                enumrating1=enumerate(csv_file1)
                readingproductlist1=list(enumrating1)
                print(readingproductlist1)      #printing out enumerated list of courier dictionaries for user selection
            courier_index_selection = int(input("Please enter a number that corresponds with your chosen courier from the list above: "))
            with open('orders.csv', mode= 'a', newline="") as file_:
                Order_status="Preparing"
                fieldnames=['Customer name', 'Customer address','Customer phone','Courier id','Status','Product IDs']
                writer = csv.DictWriter(file_, fieldnames=fieldnames)
                if file_.tell() ==0:     #if file is empty write the header/fieldnames
                    writer.writeheader()               
                writer.writerow({'Customer name':customer_name, 'Customer address':customer_address,'Customer phone':customer_phone_number,'Courier id':courier_index_selection,'Status': Order_status,'Product IDs':intergers})
            continue           # 'write in dictionary keys and match their values with user inputs'



        elif order == "3":
            orderstatus=[]
            with open("orders.csv", mode= 'r') as file4:
                csv_file4= csv.reader(file4)
                headers = next(csv_file4)
                for row in csv_file4:
                    try:
                        name= row[0]
                        order_status_=row[4]
                        orderstatus.append((name,order_status_))   
                    except IndexError:                             #index error would come up for blank lines
                        pass                                      
                neworderstatus=list(enumerate(orderstatus))
                print(neworderstatus)                #read status of all orders into an enumerated list for user to select from
            order_status_selection=int(input("Please enter a number from the list above that corresponds with the order you want to update: "))
            with open("orders.csv", mode= 'r') as file5:
                csv_file5=csv.DictReader(file5)
                readingorderslist5=list(csv_file5)
                for item in range(0,len(readingorderslist5)):             #csv file read into list of order dictionaries, we loop over them 
                    readingorderslist5[order_status_selection]["Status"]="Ready"            #we update the status of order chosen by user in the list
            with open('orders.csv', mode= 'w', newline="") as file5:
                fieldnames=['Customer name', 'Customer address','Customer phone','Courier id','Status','Product IDs']
                writer = csv.DictWriter(file5, fieldnames=fieldnames)
                if file5.tell() ==0:
                    writer.writeheader()
                writer.writerows(readingorderslist5)       #list with updated order status is written to rows
                print(f'You have updated the status of the following order:{order_status_selection} to READY')
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
            with open("couriers.csv", mode= 'r') as file_:
                csv_file = csv.DictReader(file_)
                for row in csv_file:
                    print(row)
            continue


        elif courier_choice == "2":
            courier_name = str(input("PLEASE ADD A COURIER NAME: "))
            courier_phone = int(input("PLEASE ADD A COURIER PHONE NUMBER: "))
            with open('couriers.csv', mode= 'a', newline="") as file_:
                fieldnames=['Courier name', 'Courier phone']
                writer = csv.DictWriter(file_, fieldnames=fieldnames)
                if file_.tell() ==0:      #tell file method returns current position of file, if empty then right header
                    writer.writeheader()
                writer.writerow({'Courier name':courier_name, 'Courier phone':courier_phone})
            continue
        else:
            print("YOU HAVE ENTERED THE WRONG OPTION, PLEASE TRY AGAIN")
            print("call courier menu")
        return


def productmenu():
    while True:
        product_choice = input("Please select from the following options:\nEnter (0) to return to main menu\nEnter (1) to show all products\nEnter (2) to add a new product\n")


        if product_choice ==  "0":
            mainmenu()
        

        elif product_choice == "1":
            with open("products.csv", mode = 'r') as file:
                csv_file = csv.DictReader(file)
                for row in csv_file:
                    print(row)
            continue


        elif product_choice == "2":
            product_name = str(input("PLEASE ADD A PRODUCT NAME: "))
            product_price = float(input("PlEASE ADD THE PRODUCT PRICE: "))
            with open('products.csv', mode = 'a', newline="") as file:
                fieldnames= ['Product name', 'Product price']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                if file.tell() == 0: #check if file is empty, if empty then header is written
                    writer.writeheader()
                writer.writerow({'Product name':product_name, 'Product price':product_price})
            continue


        else:
            print("YOU HAVE ENTERED THE WRONG OPTION, PLEASE TRY AGAIN")
            productmenu()
        return

def mainmenu():
    print("Welcome to the store!")
    print("Enter (0) to exit the app")
    print("Enter (1) to access the product menu\nEnter (2) to access the courier menu\nEnter (3) to access the order menu")
    choice = input()
    if choice == "0":
        print("THANKS FOR YOUR TIME, GOODBYE!")
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