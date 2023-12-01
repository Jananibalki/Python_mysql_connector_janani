file = open('lesson8.txt')
whole = file.read()
print(whole)


count = 0
for line in file:
    count = count+1
    print(line)
print(count)  

