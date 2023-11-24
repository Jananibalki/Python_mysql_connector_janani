for i in [5, 4, 3, 2, 1] :
    print(i)

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends : 
   print('Happy New Year:', friend)


largest = None
for value in [9, 41, 12, 3, 74, 15] :
    if largest is None : 
        largest = value
    elif value > largest : 
        largest = value
print( largest)

smallest = None
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None : 
        smallest = value
    elif value < smallest : 
        smallest = value
print( smallest)


found = False
for value in [9, 41, 12, 3, 74, 15] : 
   if value == 3 :
       found = True
print( found)


add = 0
count = 0
while(True):
    num = input("Enter a number : ")
    try:
        num_int = int(num)
        add = add + num_int
        count = count+1
    except:
        if(num=='done'):
            break
        else:
            print("invalid input")
            continue
print(add, count, add/count)
        
        