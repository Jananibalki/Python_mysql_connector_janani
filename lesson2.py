name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = 0
bigword = ""
for word,count in counts.items():
    if (bigcount == 0 or count > bigcount):
        bigword = word
        bigcount = count

print(bigword, bigcount)
