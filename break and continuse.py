"""i = 1
while i <= 3:
    print(i)
    if i == 3:
        break
    i += 1
print("end of loop")
x = (1, 2, 3, 4, 5)
num = 4
i
while i <= len(x):
    if x[i] == num:
        print("found")
        break
    else:
        print("not found")
    i += 1"""

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)


x = (1, 2, 3, 4, 5, 6, 7)
n = 5
i = 0
while i < len(x):
    if x[i] == n:
        print("found")
        continue
    else:
        print("not found")
    i += 1
print("end of loop")
