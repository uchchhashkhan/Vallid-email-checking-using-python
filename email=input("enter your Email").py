email=input("enter your Email : ")
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha(): #the first letter alphabet or not
        if ("@" in email) and (email.count()==1):
            if(email[-4]==".")^(email[-3]=="."):   #x-or operator(^) , beacuse xyz@in and xyz@com can't be run together
                for i in email:
                    if i == i.isspace():
                        k=1
                    elif i.isalpha():
                        if i == i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1 #if there are other signs 
                        print("Valid Email")
                if k==1 or j==1 or d==1:
                    print("Wrong 5")
            else:
                print("Wrong 4")
        else:
            print("Wrong 3")
    else:
        print("wrong 2")
else:
    print("Wrong 2")
    
