try:
    hrs = input('Enter hours:')
    hrs = float(hrs)
    rate = input('Enter rate:')
    rate = float(rate)
except:
    print('Error, please enter numeric input')
    quit()
pay = hrs * rate
if hrs > 40:
    pay += (hrs - 40) * rate * 0.5
print('Pay is:', pay)
