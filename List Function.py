print ("6,33,12,3,1,4,20,99,50,8")

print ("Choose your function from the menu! (~_^)")
print ("")
print ("Menu:")
print ("1 -> Add an element")
print ("2 -> Insert an element")
print ("3 -> Modify an element")
print ("4 -> Delete an element")
print ("5 -> Arrange in ascending order")
print ("6 -> Arrange in descending order ")

list_main=[6,33,12,3,1,4,20,99,50,8]

user=int(input("What do you want to do? "))
print("")

if user == 1:
    print("Add an Element")
    print("")
    add1=int(input("What Element would you like to add? "))
    print("")
    list_main.append(add1)
    print(list_main)
    print("")
    print("Thank You!")

if user == 2:
    print("Insert an Element")
    print("")
    element1=int(input("What Element would you like to insert? "))
    print("")
    element2=int(input("Where would you like to insert it? *Note the list starts from 0: "))
    print("")
    list_main.insert(element2,element1)
    print (list_main)
    print ("Thank You!")

if user ==3:
    print("Modify an Element")
    print("")
    modify1=int(input("Where is the element that you'd like to modify? Note the list starts from 0: "))
    print("")
    modify2=int(input("What would you like to replace it? "))
    print("")
    list_main[modify1]=modify2
    print (list_main)
    print ("Thank You!")

if user ==4:
    print("Delete an Element")
    print ("")
    delete1=int(input("What element from the list would like to delete? "))
    print("")
    list_main.remove(delete1)
    print (list_main)
    print ("Thank You!")

if user ==5:
    print("Arrange in ascending order")
    print("")
    list_main.sort()
    print(list_main)
    print ("Thank You!")

if user ==6:
    print("Arrange in descending order")
    print("")
    list_main.sort(reverse=True)
    print (list_main)
    print ("Thank You!")