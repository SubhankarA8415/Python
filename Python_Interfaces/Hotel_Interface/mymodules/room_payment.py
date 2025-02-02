def room(hotel_sele,days,voucher):
    from datetime import datetime
    curdate=datetime.now()
    curdate=str(curdate)
    month=int(curdate[5])*10+int(curdate[6])
    year=int(curdate[0])*1000+int(curdate[1])*100+int(curdate[2])*10+int(curdate[3])
    day=int(curdate[8])*10+int(curdate[9])
    a=0
    selected=[]
    price_single_bed_ac=price=int(hotel_sele[4])
    l=[["1  ","Single-bed room A/C           ",price],["2  ","Single-bed room Non-A/C       ",price-300],["3  ","Double-bedded room A/C        ",price+400],["4  ","Double-bedded room Non-A/C    ",price+100],["5  ","Four-bedded room A/C          ",price+900],["6  ","Four-bedded room Non-A/C      ",price+500],["7  ","Luxury single-bed room A/C    ",price+600],["8  ","Luxury double-bedded room A/C ",price+1100],["9  ","Luxury family room A/C        ",price+1600]]
    print("Room available are here")
    print()
    print("Sno","|","Room_Type                     ","|","Price")
    for i in l:
        print(i[0],"|",i[1],"|",i[2])
    print()
    done1=done=done5=True
    while done1:
        done2=True
        room=input("Enter the sno of the room to select-:")
        try:
            room=int(room)
            if 0<room<10:
                print("Room selected is")
                print()
                print("Sno","|","Room_Type                     ","|","Price")
                for i in l:
                    if int(i[0])==room:
                        print(i[0],"|",i[1],"|",i[2])
                        selected=i
                print()
                voucher_user=input('''Have vouchers ???
Enter voucher code to get discount upto 800
Or press enter to continue-:''')
                if voucher_user:
                    Amount=(selected[2])*days-voucher
                    print("You got a discount of",voucher)
                    print('Total price for',days,'night is',Amount)
                else:
                    Amount=(selected[2])*days
                    print('Total price for',days,'night is',Amount)
                while done2:
                    choice=input('''Enter your choice
Type 1 to proceed to payment
Or 2 to reselect room-:''')
                    if choice=="2":
                        print("Exiting to room selection")
                        done2=False
                        break
                    elif choice=="1":
                        choice2=input('''Enter the mode of payment
Type 1 for credit\debit cards (5% off)
Type 2 to pay at hotel-:''')
                        if choice2=="1":
                            Amount=(Amount*95)/100
                            while done:
                                print("Amount required to be paid is",Amount)
                                no=input('''Enter you card no
Ex-: xxxx-xxxx-xxxx-xxxx-:''')
                                if len(no)!=19:
                                    print("Invalid card no entered")
                                    continue
                                name=input("Enter name of card-:")
                                exp_date=input('''Enter expiry date of your card
Format-: MM-YYYY -:''')
                                cvv=input("Enter the cvv of your card-:")
                                otp=input("Enter the otp send to your mobile no ending with xxxxxx8912-:")
                                print("Payment successfull")
                                print("Your room has been booked succefully")
                                print("Your booking id would be sent to you via email and mobile no")
                                done1=done=done2=False
                        elif choice2=="2":
                            print("You have to pay",Amount,"rs at the hotel")
                            code=input("Enter the code sent to your mobile to confirm your booking-:")
                            print("Your room has been booked succefully")
                            print("Your booking id would be sent to you via email and mobile no")
                            done=done1=done2=False
                            a=1
                            break
                        else:
                            print("Please select from above choices only")
                            continue
        except:
            print("Please select from the above options only")
            continue
        return Amount,selected,done,a
                                
                                
                                    
                                        
                                
                                
                            
