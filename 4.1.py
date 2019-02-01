def computepay(hrs, rate):
    hrs = float(hrs)
    rate = float(rate)
    pay = hrs * rate
    if hrs > 40:
        pay += (hrs - 40) * rate * 0.5
    return pay


hrs = input('Enter hours:')
rate = input('Enter rate:')
print(computepay(hrs, rate))
