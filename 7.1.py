fhand = open('mbox-short.txt', 'r')
count = 0
for string in fhand:
    count = count + 1
    string = string.rstrip().upper()
    print(string)
print('Line count:', count)
