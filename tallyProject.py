from turtle import *

#Count the number of people
def countPeople():
    numberOfPeople=int(input("Enter the number of people in your group: "))


numOfPeople=int(input("Enter the number of people in your group: "))
numOfLoops=1
#Draw a representation for everyone
for i in range(1,(numOfPeople+1),1):
    #Draw a diagonal for every five people
    if (numOfLoops%5)!=0:
        # #Draw asingle line for an individual person
        pendown()
        left(90)
        forward(25)
        penup()
        back(25)
        #move to the next person
        right(90)
        forward(6)
        pendown()

        #draw a diagonal for every five people
    else:
        penup()
        left(90)
        forward(25)
        left(90)
        forward(28)
        left(135)
        pendown()
        forward(37.537)
        left(45)
        penup()
        forward(12)
        pendown()

    numOfLoops+=1


input("Enter Anything her and hit ENTER to stop: ")


#Move the turtle from one tally to the next


