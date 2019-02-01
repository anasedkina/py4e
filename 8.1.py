fhand = open('romeo.txt')
list_of_words = list()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in list_of_words:
            list_of_words.append(word)
list_of_words.sort()
print(list_of_words)
