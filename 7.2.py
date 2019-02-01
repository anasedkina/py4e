fname = input('Enter the file name:')
count = 0
sum = 0
try:
    fhand = open(fname, 'r')
except:
    print('Bad file name', fname)
    if fname == 'na na boo boo':
        print('NA NA BOO BOO TO - You have been pank\'d')
    quit()
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        atpos = line.find(':')
        num = line[atpos + 1:]
        num = float(num)
        sum = sum + num
print('There are', count, 'lines')
print('The average spam confidence:', sum / count)
