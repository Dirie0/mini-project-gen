import csv
def couriermenu():
    while True:
        courier_choice = input("Please select from the following options:\nEnter (0) to return to main menu\nEnter (1) to show all couriers\nEnter (2) to add a new courier\n")
        if courier_choice ==  "0":
            print("call main menu")
        elif courier_choice == "1":
            with open("couriers.csv", mode= 'r') as file_:
                csv_file = csv.DictReader(file_)
                readingcourierlist = list(csv_file)
                print(readingcourierlist)
            continue
        elif courier_choice == "2":
            courier_name = str(input("PLEASE ADD A COURIER NAME: "))
            courier_phone = int(input("PLEASE ADD A COURIER PHONE NUMBER: "))
            with open('couriers.csv', mode= 'a', newline="") as file_:
                fieldnames=['Courier name', 'Courier phone']
                writer = csv.DictWriter(file_, fieldnames=fieldnames)
                if file_.tell() ==0:
                    writer.writeheader()
                writer.writerow({'Courier name':courier_name, 'Courier phone':courier_phone})
            continue
        else:
            print("YOU HAVE ENTERED THE WRONG OPTION, PLEASE TRY AGAIN")
            print("call courier menu")
        return
couriermenu()
