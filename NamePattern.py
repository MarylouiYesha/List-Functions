#y
for row in range (7):
    for col in range (5):
        if (col ==2 and row>1) or (row==col and col<2) or (row==0 and col==4) or (row==1 and col==3):
            print ("*", end=" ")
        else:
            print (end= " ")
    print ()
#e
for row in range (7):
    for col in range (5):
        if col==0 or ((row==0 or row==3 or row==6) and (col>0)):
            print ("*",end= " ")
        else:
            print (end= " ")
    print ()
#s
for row in range(7):
    for col in range (6):
        if ((row==0 or row==3 or row==6) and (col>0 and col<4)) or (col==0 and (row>0 and row<3))or (col==5 and (row>3 and row<6)):
            print("*", end=" ")
        else:
            print (end=" ")
    print ()
#h
for row in range (7):
    for col in range (6):
        if col==0 or col==5 or (row==3 and (col>0 and col<5)):
            print("*", end="")
        else:
            print (end=" ")
    print () 
#a
for row in range (7):
    for col in range (5):
        if((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*", end="")
        else:
            print (end=" ")
    print ()

