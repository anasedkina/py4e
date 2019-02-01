largest = None
smallest = None
sum = 0
count = 0
while True:
    num = input('')
    if num == 'done':
        break
    try:
        num = float(num)
    except:
        print('Bad input')
        continue
    count = count + 1
    sum = sum + num
    if smallest is None or num < smallest:
        smallest = num
    if largest is None or num > largest:
        largest = num
print(count, sum, largest, smallest)
