hours = int(input("enter hours : "))
rate = int(input("enter rate : "))

if (hours <= 40):
    pay = hours * rate
else:
    regulartime = 40
    overtime = hours - 40
    pay = (regulartime * rate) + (overtime * 1.5 * rate)

print("pay = ", pay)

#///////////////////////////////////////////

hour = input("enter hours : ")
rate = input("enter rate : ")

try:
    a=int(hour)
except:
    print("Error, please enter numeric input")
    
try:
    b=int(rate)
except:
    print("Error, please enter numeric input")

#/////////////////////////////////////

score = input("enter score between 0.0 to 1.0 : ")

try:
    score = float(score)
    
    if(score >= 0.9):
        print("A")
    elif(score >= 0.8):
        print("B")
    elif(score >= 0.7):
        print("C")
    elif(score >= 0.6):
        print("D")
    elif(score < 0.6):
        print("F")
    else:
        print("Bad score")
except:
    print("Bad score")