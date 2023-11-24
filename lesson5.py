def computepay(hours, rate):
    
    if(hours <=  40):
        pay = hours * rate
        return pay
    else:
        regulartime = 40
        overtime = hours - 40
        pay = (regulartime * rate) + (overtime * 1.5 * rate)
        return pay
    
hours = int(input("enter hours : "))
rate = int(input("enter rate : "))
pay = computepay(hours, rate)

print("pay = ",pay)

#//////////////////////////////////

def computegrade(score):
    
    try:
        score = float(score)
    
        if(score >= 0.9):
            return "A"
        elif(score >= 0.8):
            return "B"
        elif(score >= 0.7):
            return "C"
        elif(score >= 0.6):
            return "D"
        elif(score < 0.6):
            return "F"
        else:
            return "Bad score"
    except:
        return "Bad score"
    
score = input("enter score between 0.0 to 1.0 : ")
grade = computegrade(score) 
print("grade = ", grade)