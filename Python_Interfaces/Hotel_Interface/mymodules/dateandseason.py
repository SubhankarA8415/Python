def dateseason():
    from datetime import datetime
    curdate=datetime.now()
    curdate=str(curdate)
    month=int(curdate[5])*10+int(curdate[6])
    year=int(curdate[0])*1000+int(curdate[1])*100+int(curdate[2])*10+int(curdate[3])
    day=int(curdate[8])*10+int(curdate[9])
    right=True
    while right:
            print("Enter your checkin date to proceed")
            dateuser1=input("Format dd-mm-yyyy-:")
            try:
                year2=int(dateuser1[6])*1000+int(dateuser1[7])*100+int(dateuser1[8])*10+int(dateuser1[9])
                month2=int(dateuser1[3])*10+int(dateuser1[4])
                day2=int(dateuser1[0])*10+int(dateuser1[1])
                if year2%4==0:
                    if year2%100==0:
                         if year2%400==0:
                                monthdays={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
                         else:
                                monthdays={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
                    else:
                         monthdays={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
                else:
                    monthdays={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            except:
                print("The check in date entered is in wrong format please try again")
                continue
            if month2 > 12 or month2 < 1:
                print("You have entered wrong month please try again")
                right=True
                continue
            if day2 > monthdays[month2] or day2 < 0:
                print("You have entered wrong date please try again")
                right=True
                continue
            if year == year2:
                if month>month2:
                         print("You have entered past month please try again")
                         continue
                elif month==month2:
                         if day>=day2:
                            print("You have entered past or current date please try again")
                         else:
                            right=False
                else:
                    right=False
            elif year>year2:
                print("You have entered past year please try again")
                continue
            else:
                right=False
                break
    day1,month1,year1=day2,month2,year2
    sum1=year1+(month1*100)+day1
    datein=dateuser1
    if 1<month1<=3:
        season="Pre winter"
    elif 3<month1<=5:
        season="Spring"
    elif 5<month1<=7:
        season="Summer"
    elif 7<month1<=9:
        season="Rainy"
    elif 9<month1<=10:
        season="Autumn"
    else:
        season="Winter"
    right=True
    while right:
            print("Enter your checkout date to proceed")
            dateuser2=input("Format dd-mm-yyyy-:")
            try:
                year2=int(dateuser2[6])*1000+int(dateuser2[7])*100+int(dateuser2[8])*10+int(dateuser2[9])
                month2=int(dateuser2[3])*10+int(dateuser2[4])
                day2=int(dateuser2[0])*10+int(dateuser2[1])
                if year2%4==0:
                    if year2%100==0:
                         if year2%400==0:
                                monthdays={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
                         else:
                                monthdays={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
                    else:
                         monthdays={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
                else:
                    monthdays={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            except:
                print("The check out date entered is in wrong format please try again")
                continue
            sum2=year2+(month2*100)+day2
            if (year2-year1)==0:
                if sum2<=sum1:
                    print("Checkout date is smaller or equal to checkin date please enter again")
                    right=True
                    continue
                else:
                    right=False
            if month2 > 12 or month2 < 1:
                print("You have entered wrong month please try again")
                right=True
                continue
            if day2 > monthdays[month2] or day2 < 0:
                print("You have entered wrong date please try again")
                right=True
                continue
            if year == year2:
                if month>month2:
                         print("You have entered past month please try again")
                         continue
                elif month==month2:
                         if day>=day2:
                            print("You have entered past or current date please try again")
                         else:
                            right=False
                else:
                    right=False
            elif year>year2:
                print("You have entered past year please try again")
                continue
            if (year2-year1)>1:
                print("Year gap is too large please enter again")
                right=True
                continue
            elif (year2-year1)==0:
                if (month2-month1)>1:
                    print("Month difference is too large please try again")
                    right=True
                    continue
                else:
                    right=False
            elif (year2-year1)==1:
                if (month1-month2)!=11:
                    print("Month difference is too large please try again")
                    right=True
                    continue
                else:
                    right=False
            else:
                right=False
                break
    dateout=dateuser2
    if month1==month2:
        days=day2-day1
    else:
        days=(monthdays[month1]-day1)+day2
    return datein,dateout,season,days



