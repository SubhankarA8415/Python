def loginuser():
    import pickle
    f=open("login.dat",'ab+')
    f.seek(0)
    l=[]
    while True:
        try:
            l.append(pickle.load(f))
        except:
            break
    done=False
    done2=True
    while True:
        if done:
            break
        user=input('''Press 1 to login
Or new user ?? Press 2 to create account-:''')
        if user=="1":
            while done2:
                username=input("Enter your user name-:")
                password=input("Enter your password-:")
                for i in l:
                    if i["name"]==username:
                        if i["password"]==password:
                            print("Logged in as",username)
                            done=True
                            done2=False
                            break
                    else:
                        print("Username or password is incorrect")
                        choice=input('''Wanna try again
Press 1 to try again
Or Press 2 to exit login-:''')
                        if choice=="1":
                            continue
                        elif choice=="2":
                            break
                        else:
                            print("Please press one or two only")
                            continue
        elif user=="2":
            while True:
                    username=input("Enter a username to continue-:")
                    password=input("Create a password to continue-:")
                    email=input("Enter your email-:")
                    user12=False
                    for i in l:
                        if i["name"]==username:
                            print('''Username already exists
Please try some other''')
                            user12=True
                    if user12:
                        a=input('''Are you that previous user ??
Press 1 to login with password
Or Press 2 to try some other-:''')
                        if a=="1":
                            break
                        elif a=="2":
                            continue
                        else:
                            print('''Please choose between 1 or 2 only
Going back to sign in page''')
                            continue

                    else:    
                        pickle.dump({"name":username,"password":password,"Email":email},f)
                        f.flush()
                        print("Logged in as",username)
                        done=True
                        break
        else:
            print("Please select from the above options only")
    f.close()
    return

