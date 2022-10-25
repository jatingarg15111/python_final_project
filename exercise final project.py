import json
d=open('inventory.json')
dfruits = json.load(d)
d.close()
bfruits = {}
while (True):
    print("Welcome to the grocery store")
    print("1. Display Inventory")
    print("2. Buy Fruits")
    print("3. Stock Fruits")
    print("4. Exit")
    choice = int(input("Please enter a choice 1, 2, 3, or 4: "))
    if choice == 1:
        d=open('inventory.json')
        dfruits = json.load(d)
        d.close()
        if dfruits:
            print("ID", "Fruit Name","P_price", "Quantity", "S_Price", sep="    ")
            for k,v in dfruits.items(): 
                print(k,v["desc"], v["p_price"], v["quantity"], v["s_price"], sep="    ")
        else:
            print("We don't have any stock")
    elif choice == 2:
        d=open('inventory.json')
        dfruits = json.load(d)
        d.close()
        while(True):
            fruit = input("Which Fruit (ID) you want to buy ( Enter 0 for done ) : ")
            if fruit =="0":
                break
                         
            else:
                while fruit not in dfruits:
                    print("We don't have", fruit, "in our stock.")
                    fruit = input("Which Fruit (ID) you want to buy ( Enter 0 for done ) : ")
                qty = int(input("How many ?"))
                while qty > dfruits[fruit]["quantity"] or qty <= 0:
                        print("We don't have", qty, dfruits[fruit]["desc"] , "in our stock.")
                        qty = int(input("How many ?"))
                print(qty,"of",dfruits[fruit]["desc"] , "has/have been invoiced.")
                dfruits[fruit]["quantity"] -= qty
                s=dfruits[fruit]["s_price"]
                p=qty
                z=s*p
                if fruit not in bfruits:
                    bfruits[fruit]={"desc":dfruits[fruit]["desc"], "quantity":qty, "s_price":dfruits[fruit]["s_price"], "total_price":z}
                else :
                    bfruits[fruit]["quantity"] += qty
        print("Your total invoiced fruits are :")
        print("ID", "Fruit Name", "Quantity", "Price", "Total price", sep="    "   )
        for k,v in bfruits.items():
            print(k,v["desc"], v["quantity"], v["s_price"], v["total_price"], sep="     ")
        print("New stocked up inventory is :")
        print("ID", "Fruit Name","P_price", "Quantity", "S_Price", sep="    ")
        for k,v in dfruits.items(): 
            print(k,v["desc"], v["p_price"], v["quantity"], v["s_price"], sep="    ")
        d=open('inventory.json', 'w')
        dfruits=json.dump(dfruits, d)
        d.close()
    elif choice == 3:
        d=open('inventory.json')
        dfruits = json.load(d)
        d.close()
        while (True):
            fruit = input("Which Fruit (ID) you want to buy ( Enter 0 for done ) : ")
            if fruit == "0":
                break
            else:
                if fruit not in dfruits:
                    name = input("Enter fruit name : ")
                    p_price = float(input("Enter purchasing price : $"))
                    qty = int(input("How many ?"))
                    s_price = float(input("Enter selling price : $"))
                else:
                    qty = int(input("How many ?"))
                if fruit not in dfruits:
                    dfruits[fruit]={"desc":name, "p_price":p_price, "quantity":qty, "s_price":s_price}
                else:
                    dfruits[fruit]["quantity"] += qty
        print("New stocked up inventory is :")
        print("ID", "Fruit Name","P_price", "Quantity", "S_Price", sep="    ")
        for k,v in dfruits.items(): 
            print(k,v["desc"], v["p_price"], v["quantity"], v["s_price"], sep="    ")
        d=open('inventory.json', 'w')
        dfruits=json.dump(dfruits, d)
        d.close()
    elif choice == 4 :
            print("Exit")
            print("Thank You.")
            break
            exit()
    else :
        print("Your input is wrong. Please put the right number")
        
            
        
            
        
                

                
