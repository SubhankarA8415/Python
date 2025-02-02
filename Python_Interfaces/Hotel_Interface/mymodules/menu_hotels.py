def menu():
    import csv
    l=[]
    l2=[]
    l3=[]
    f=open("Breakfast_snacks.csv","r")
    reader=csv.reader(f)
    for i in reader:
        l.append(i)
    f.close()
    f=open("lunch_dinner.csv","r")
    reader=csv.reader(f)
    for i in reader:
        l2.append(i)
    f.close()
    f=open("Drink_sweets.csv","r")
    reader=csv.reader(f)
    for i in reader:
        l3.append(i)
    f.close()
    return l,l2,l3

 
       
