import random
from datetime import datetime
from mymodules import login
from mymodules import dateandseason
from mymodules import menu_hotels
login.loginuser()
from mymodules import hotels_view
from mymodules import room_payment
bre_sna=lun_din=drin_swee=()
hotel_sele=[]
voucher=random.randint(500,800)
bid=random.randint(500000,600000)
print("\\\\\\\\\\***************//////////HOTELS\\\\\\\\\\***************//////////Travelodge_inn\\\\\\\\\\***************//////////")
w=input("Welcome to HOOKS.in press enter to access hotels")
while True:
    city=input("Enter name of city to continue-:")
    city=city.capitalize()
    print("Welcome to",city,"Sir\Madam")
    done=True
    while done:
        budget=input('''Please select your budget
Press 1 for under 5000
Press 2 for under 10000
Press 3 for under 100000-:''')
        if budget=="1":
            price=5000
        elif budget=="2":
            price=10000
        elif budget=="3":
            price=100000
        else:
            print("PLease select from the above options only")
            continue
        print("List of hotels available are")
        print()
        avb_tags,hotels_list=hotels_view.hotel_view(price)
        print()
        choice=input('''Enter the tag to select the hotel
Or press 1 to return to budget section-:''')
        if choice=="1":
            continue
        else:
            try:
                choice=int(choice)
                if choice in avb_tags:
                    tag=choice
                    for i in hotels_list:
                        if int(i[3])==tag:
                            print("Hotel selected is")
                            print()
                            print("Sno ","|","Name_of_hotel                 ","|","Rating","|","Tag","|","Price")
                            print(i[0],"|",i[1],"|",i[2],"|",i[3],"|",i[4])
                            print()
                            print("Facilities available are-:")
                            print("Wi-Fi","|","Parking","|","Laundry","|","Spa","|","Swimming pool","|","TV","|","Room service")
                            hotel_sele=i
                    done=False
                    break
                else:
                    print("Please select from the above options only")
            except:
                print("Please select from the above options only")
    date=dateandseason.dateseason()
    days=date[3]
    print("Booking season is",date[2])
    name=input("Please enter your full name-:")
    while True:
        try:
            phone=int(input("Enter your mobile number-:"))
            if len(str(phone))!=10:
                print("Wrong phone no entered")
                continue
            else:
                break
        except:
            print("Wrong phone no entered")
            continue
    email=input("Enter your email id-:")
    done=True
    while done:
        while True:
            d=int(input("Press 1 to select rooms or press 2 to see the menu-:"))
            if d==2:
                print("Welcome to menu site")
                print("Here is the menu of the hotel")
                print()
                print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Breakfast_Snacks////////////////////////////////////")
                print()
                bre_sna,lun_din,drin_swee=menu_hotels.menu()
                for i in bre_sna:
                    print(i[0],"|",i[1],"|",i[2],"|",i[3],"|",i[4],"|",i[5],"|",i[6],"|")
                print()
                print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Lunch_Dinner/////////////////////////////////////////////////////////")
                print()
                for i in lun_din:
                    print(i[0],"|",i[1],"|",i[2],"|",i[3],"|",i[4],"|",i[5],"|",i[6],"|",i[7],"|",i[8],"|",i[9],"|")
                print()
                print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Drinks_Sweets//////////////////////////////////////////////////////")
                print()
                for i in drin_swee:
                    print(i[0],"|",i[1],"|",i[2],"|",i[3],"|",i[4],"|",i[5],"|",i[6],"|",i[7],"|",i[8],"|")
                print()
                continue
            elif d==1:
                print("Welcome to booking site")
                Amount,selected,done,a=room_payment.room(hotel_sele,days,voucher)
                break
    if a==1:
        Paid="Pending"
    else:
        Paid="Paid"
    print("Your booking id is here")
    print()
    print("Name of hotel-: ",hotel_sele[1]," | ","Price for one night-:",selected[2],"rs")
    print()
    print("Name of guest-:",name," | ","Mobile no-:",phone," | ","email-:",email)
    print()
    print("Checkin date-:",date[0]," | ","Checkout date-:",date[1]," | ","Total no of days-:",date[3]," | ","Booking season-:",date[2])
    print()
    print("Hotel facilities-:","Wi-Fi","|","Parking","|","Laundry","|","Spa","|","Swimming pool","|","TV","|","Room service"," | ","Location-:",city)
    print()
    print("Room selected-:",selected[1]," | ","Booking i_d-:",bid," | ","Total amount-:",Amount," | ","Payment status-:",Paid)
    print()
    print("Booked at-:",datetime.now())
    print()
    choice=input("Want to book more room ? type yes or no-:")
    choice=choice.lower()
    if choice=="no":
        break
print("Thanks for using us")
print('''For any issues regarding site
Developer e-mail-hotel@gmail.com
Please contact through the above mentioned e-mail
Developed by-: Subhankar Pandit
(This project is just an demo of some real and generated data, but the email provided is not real''')

