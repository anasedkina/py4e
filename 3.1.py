hrs = input('Enter hours:')
rate = input('Enter rate:')
hrs = float(hrs)
rate = float(rate)
pay = hrs * rate
if hrs > 40:
    pay += (hrs - 40) * rate * 0.5
print('Pay is:', pay)
