#Lesson 15

#Example 1
x=int(input("how much phones do you have"))

match x:
    case 0:
        print("HAHA,you have no phone")
    case 1:
        print("HAHA, you just have one phone")
    case 2:
        print("congrats you have 2 phones")
    case 3:
        print("are you a spy?")

#Example 2
def trafficlight(colour):
    colour=colour.lower()
    match colour:
        case "green":
            print("Go")
        case "yellow":
            print("stop if you can")
        case "red":
            print("stop")
trafficlight("red")

#Example 3
def day(number):
    match number:
        case 1:
            print("monday")
        case 2:
            print("tuesday")
        case 3:
            print("wednesday")
        case 4:
            print("thursday")
        case 5:
            print("friday")
        case 6:
            print("saturday")
        case 7:
            print("sunday")
        case 0:
            print("sunday")
day(7)#test

