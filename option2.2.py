##Option 2 - App Engine
##Build a simple webapp, using Google App Engine that provides users with an ability to keep
##track of a shopping list
##● Should be written in Python, Go, or Java.
##● User must be able to add, delete and edit an item to the shopping list
##● User must be able to view their whole shopping list
##● User must be able to delete their whole shopping list (in addition to deleting individual
##items)
##● Each user must be able to login with their Google account and their shopping list must
##persist between their logins
##Some resources
##https://cloud.google.com/appengine/docs/python/getting-started/creating-guestbook

print("""
 __     __                    _____  _                           _                 _  _       _   
 \ \   / /                   / ____|| |                         (_)               | |(_)     | |  
  \ \_/ /___   _   _  _ __  | (___  | |__    ___   _ __   _ __   _  _ __    __ _  | | _  ___ | |_ 
   \   // _ \ | | | || '__|  \___ \ | '_ \  / _ \ | '_ \ | '_ \ | || '_ \  / _` | | || |/ __|| __|
    | || (_) || |_| || |     ____) || | | || (_) || |_) || |_) || || | | || (_| | | || |\__ \| |_ 
    |_| \___/  \__,_||_|    |_____/ |_| |_| \___/ | .__/ | .__/ |_||_| |_| \__, | |_||_||___/ \__|
                                                  | |    | |                __/ |                 
                                                  |_|    |_|               |___/
                                                  """)

yes = ['yes','YES','Yes','Y','y', 'OK']    
no = ['no','No','NO','N','n']
shoppinglist = []
try:
    with open('ShoppingList.txt', 'r') as readfile:  
        filecontents = readfile.readlines()

    for line in filecontents:   
        current_place = line[:-1]   #removes line break
        shoppinglist.append(current_place)
except:
    shoppinglist = []

def start():
    global shoppinglist
    while True:
        print("""What would you like to do?

        1.   View your shopping list
        2.   Add an item to the shopping list
        3.   Edit an item in the shopping list
        4.   Delete an item from the shopping list
        5.   Delete your whole shopping list
        """)

        while True:
            try:
                userchoice = int(input(""))
                break
            except:
                print("Please enter a number")

        if userchoice == 1:
            print("Here is your shopping list:\n " + '\n '.join(shoppinglist))
            
        elif userchoice == 2:
            while True:
                itemtoadd = input("Enter the details to add to the shopping list\n")
                shoppinglist.append(itemtoadd)
                print("\nHere is your shopping list:\n " + '\n '.join(shoppinglist))
                if input("Would you like to add another item?\n") in yes:
                    pass
                else:
                    break
            
        elif userchoice == 3:
            print("Here is your shopping list:\n " + '\n '.join(shoppinglist))
            edititem = input("What would you like to edit? Use the actual word.\n")
            newitem = input("What would you like to replace it with?\n")
            try:
                shoppinglist[shoppinglist.index(edititem)] = newitem
            except:
                print("This could not be completed. Try using the full description.")
            print("Here is your shopping list:\n " + '\n '.join(shoppinglist))
            
            
        elif userchoice == 4:
            print("Here is your shopping list:\n " + '\n '.join(shoppinglist))
            deleteitem = input("What would you like to delete? Use the actual word.\n")
            try:
                shoppinglist.remove(deleteitem)
                print("Here is your shopping list:\n " + '\n '.join(shoppinglist))
            except:
                print("This item does not exist")
            
        elif userchoice == 5:
            if input("Are you sure that you want to delete your whole shopping list?\n") in yes:
                shoppinglist = []
            
        else:
            print("This is not a suitable input, please try again. ")
        again()
        break  

def again():
    again = input("\nDo you want to select another option?\n")
    if again in yes:
        start()

start()
print("Here is your shopping list:\n " + '\n '.join(shoppinglist))
with open("ShoppingList.txt", "w+") as writefile:
    writefile.writelines("%s\n" % x for x in shoppinglist)

