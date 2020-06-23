## FIND THE ARMSTRONG NUMBERS IN THE RANGE 100 TO 5000 ##

low_lmt = 100
upp_lmt = 5000
temp = 0
arm = []

for i in range(low_lmt, upp_lmt+1):
    n = len(str(i))
    temp = i
    s = 0
    for j in range(0, n):
      s += pow((temp % 10), n)
      temp //= 10

    if s == i:
        arm.append(i)

print('Armstrong numbers in the range 100 to 5000 are :-')
print(arm)