age = 20
if (age >= 18):
    print("this is will be vota")


Light = "red"
if (Light == "green"):
    print("you can drive ")
elif (Light == "yallow"):
    print("wite for car")
elif (Light == "red"):
    print("stop")
num = 20
if (num > 21):
    print("20 is grter than 15")
elif (num > 22):
    print("this is also greater than 16 ")
else:
    print("is equal to 20")


age2 = int(input("enter you are age "))
if (age2 >= 18):
    print("you can vota ")
else:
    print("you cannot be vote")

marks = int(input("inter you are marks "))
if (marks >= 90 and marks <= 80):
    print("grade=A")
elif (marks >= 80 and marks <= 70):
    print("grade B")
elif (marks >= 70 and marks <= 60):
    print("grade C")
else:
    print("fail")

age3 = int(input("enter you age"))
if (age3 >= 20):
    if (age3 >= 80):
        print("you cannot drive")
    else:
        ("you can drive")
else:
    print("child")


num = int(input("enter you are number "))
if num % 2 == 0:
    print("even")
elif num % 2 == 1:
    print("odd")

num1 = int(input("enter you are number1 "))
num2 = int(input("enter you are number2 "))
num3 = int(input("enter you are number3 "))
if num1 > num2 and num3:
    print("number 1 greter")
elif num1 < num2 and num3:
    print("number1 lass than ")

    

num1 = int(input("enter you are number1 "))
num2 = int(input("enter you are number2 "))
num3 = int(input("enter you are number3 "))
num4 = int(input("enter you are number4 "))

if num1 > num2 and num1 > num3:
    print("number 1 is greater", num1)
elif num2 > num3 and num2 > num4:
    print("number 2 is greater", num2)
elif num3 > num4:
    print("number 3 is greater", num3)
else:
    print("number 4 is greater than ", num4)


x = int(input("enter you number "))
if x % 7 == 0:
    print("multiply of seven")
else:
    print("not multip in seven")


year = int(input("enter year"))
if year % 400 == 0:
    print("leap year")
else:
    print("not leap year")

chr1 = (input("checter"))
if chr1 in aeiou:
    print("vawal")
