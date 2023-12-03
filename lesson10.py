a = dict(janani = 1)
b = ['janani', 'janani', 'sahana', 'balaji']

for name in b:
    if name not in a:
        a[name] = 1   
    else:
        a[name] = a[name] + 1
print(a)


sen = input("enter a sentence : ")

a = sen.split()
d = {}
for word in a:
    d[word] = d.get(word, 0 ) + 1
print(d)


d = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
for key in d.keys():
    print(key, d[key])
    
print()

for value in d.values():
    print(value)
    
print()

for key,value in d.items():
    print(key, value)

