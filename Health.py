import datetime

def getdate():
    return datetime.datetime.now()

def add_func(client):
    if client == "1":
        exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
        add_item = input("What do you want to Add? : ")
        if exer_diet == "1":
            with open("harry_exer.txt","a") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    f.write("%s" % item) 
            print("Item successfully added")        
        elif exer_diet == "2":
            with open("harry_diet.txt","a") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    f.write("%s" % item) 
            print("Item successfully added")          
    elif client == "2":
        exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
        add_item = input("What do you want to Add? : ")
        if exer_diet == "1":
            with open("rohan_exer.txt","a") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    f.write("%s" % item) 
            print("Item successfully added")        
        elif exer_diet == "2":
            with open("rohan_diet.txt","a") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    f.write("%s" % item) 
            print("Item successfully added")         
    elif client == "3":
        exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
        add_item = input("What do you want to Add? : ")
        if exer_diet == "1":
            with open("hammad_exer.txt","a") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    f.write("%s" % item) 
            print("Item successfully added")        
        elif exer_diet == "2":
            with open("hammad_diet.txt","a") as f:
                add = [" [",getdate(),"] ",add_item,"\n"]
                for item in add:
                    f.write("%s" % item) 
            print("Item successfully added") 
def retrive_func(client):
    if client == "1":
        exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
        if exer_diet == "1":
            try:
                with open("harry_exer.txt","r") as f:
                    print("\nFile items\n")
                    for i in (f.readlines()):
                        print(i)
            except:
                print("Items does not retrieve. Please add some items in file")        
        elif exer_diet == "2":
            try:
                with open("harry_diet.txt","r") as f:
                    print("\nFile items\n")
                    for i in (f.readlines()):
                        print(i) 
            except:
                print("Items does not retrieve. Please add some items in file")                
    elif client == "2":
        exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
        if exer_diet == "1":
            try:
                with open("rohan_exer.txt","r") as f:
                    print("\nFile items\n")
                    for i in (f.readlines()):
                        print(i)
            except:
                print("Items does not retrieve. Please add some items in file")         
        elif exer_diet == "2":
            try:
                with open("rohan_diet.txt","r") as f:
                    print("\nFile items\n")
                    for i in (f.readlines()):
                        print(i)
            except:
                print("Items does not retrieve. Please add some items in file")         
    elif client == "3":
        exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
        if exer_diet == "1":
            try:
                with open("hammad_exer.txt","r") as f:
                    print("\nFile items\n")
                    for i in (f.readlines()):
                        print(i)
            except:
                print("Items does not retrieve. Please add some items in file")         
        elif exer_diet == "2":
            try:
                with open("hammad_diet.txt","r") as f:
                    print("\nFile items\n")
                    for i in (f.readlines()):
                        print(i)
            except:
                print("Items does not retrieve. Please add some items in file")          

client = input("Enter number 1 for harry, 2 for rohan and 3 for hammad : ") 
add_retrieve = input("Enter number 1 for Add and 2 for Retrieve : ")

if add_retrieve == "1":
    add_func(client)
elif add_retrieve == "2":
    retrive_func(client)
