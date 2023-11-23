'''filename = input("enter file name : ")
content=open(filename, "r")
#print(open(filename, "r").read())
count=dict()
for line in content:
    words = line.split()
    for word in words:
        count[word] = count.get(word,0) + 1

bigcount=0
for keys,values in count.items():
    if(values == bigcount or values > bigcount):
        bigcount = values
        bigword = keys

print("Highest count " , bigcount)
print("word = ", bigword)'''

#////////////////////////////////

'''width = 17
height = 12.0
print(width//2) 

print(width/2.0)

print(height/3)

print(1 + 2 * 5)'''

#///////////////////////////////////

'''name = input("enter your name : ")
print("hello ",name)'''

#//////////////////////////////////////////

'''hours = input("enter hours : ")
rate = input("enter rate : " )
print("pay = ", int(hours)*float(rate))'''


#///////////////////////////

'''celsius =  int(input("enter celsius temperature : "))
fah = celsius*(9/5) + 32
print("fahrenheit temp is ",int(fah))'''



        
