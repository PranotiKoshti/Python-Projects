""" GET THE LONGEST STREAK OF 1s IN AN ARRAY """

a = [1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0]
n = len(a)
c1 = cnt = 0
for i in range(n):
    if a[i] == 1:
        c1 += 1
    if a[i] == 0 or i == (n-1):
        cnt = max(c1, cnt)
        c1 = 0

print(f'No. of 1s in given array = {cnt}')