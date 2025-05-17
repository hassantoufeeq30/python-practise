list1 = [1, 2, 3, 4, 5, 6, 7]
for i in list1:
    print(i)

    s = (1, 3, 4, 5, 6, 7, 8, 9, 10)
    x = 4
    for l in s:
        print(l)
        if l == 5:
            break
        else:
            print("not found")
print("end of loop")




str = {"hello", "world", "python"}
for char in str:
    print(char)
    

str = ("hassan")
for char in str:
    if char == 'n':
        print("fond a chers")

        break
    print(char)

else:
    print("end of loop ")


    


l = [3, 3, 4, 4, 6, 7, 8, 9, 0, 10]

for i in l:
    if i == l[6]:
        print("x is fond")
        break
    print(i)
print("end of loop ")

print(range(10))



seq = range(10)
for i in seq:
    print(i)

    

 for i in range(2, 10, 2):
 print(i)

for i in range(10, ):
    print(i)
    


for i in range(1, 100):
    print(i)

    

for i in range(100, -1, -1):
    print(i)
    

x = int(input("enter a number"))
for i in range(1, 11):
    
    print(f"{x}*{i}={x*i}")
    




n = 6
sum = 0
while sum <= n:
    print(n*(n+1)//2)
    sum += 1
    print(sum)


    

x = 5
add = 0
for i in range(1, x+1):
    add += i
print(add)



n = 4
f = 1
i = 1
while i <= n:
    f *= i
    i += 1
print("the facto", f)


n = 4
f = 1
for i in range(1, n+1):
    f *= i
    print(i)
print("factorila", f)
