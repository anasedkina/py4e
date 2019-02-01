str = 'X-DSPAM-Confidence:0.847512'
atpos = str.find(':')
print(atpos)
num = str[atpos + 1:]
num = float(num)
print(num)
