def hotel_view(price):
    import csv
    f=open("hotellist.csv","r")
    reader=csv.reader(f)
    l=[]
    l2=[]
    print("Sno ","|","Name_of_hotel                 ","|","Rating","|","Tag","|","Price")
    for i in reader:
        if int(i[4])<price:
            print(i[0],"|",i[1],"|",i[2],"|",i[3],"|",i[4])
            l.append(int(i[3]))
            l2.append(i)
    f.close()
    return l,l2

        
        
