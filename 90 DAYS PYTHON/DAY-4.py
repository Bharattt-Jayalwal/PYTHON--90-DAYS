#DAY 4 OF 90 DAYS---Conditions

#1)
a=12
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")

#2)
a=80
if a%2==0:
    print("Even")
else:
    print("odd")

#3)
age=int(input("Enter age:"))
if age<18:
    print("Minor")
else:
    print("adult")

#4)
marks=60
if marks>=40:
    print("Pass")
else:
    print("Fail")

#5)
num1=12
num2=23
if num1==num2:
    print("Equal")
else:
    print("DIfferent")

#6)
num1=int(input("Enter number 1:"))
if num1%5==0:
    print("Number is divisible by 5")
else:
    print("not divisible by 5")

#7)
Marks=int(input("Enter marks:"))
if Marks>=90<100:
    print("Grade A+")
if Marks<90>=80:
    print("Grade A")
if Marks>=79<70:
    print("Grade B")
if Marks<=60>69:
    print("Grade C")
if Marks<=50>59:
    print("Grade D")
else:
    print("FAIL")

#8)
Age=int(input("Enter age:"))
Percentage=float(input("Enter percentage:"))
Entrance_Score=int(input("Enter Score:"))
if Age>=17 and Percentage>=60 and Entrance_Score>=50:
    print("Eligible")
else:
    print("not eligible")

#9)
username=input("Enter username:")
password=str(input("Enter password:"))
if username=="Bharat" and password=="Bha123":
    print("Pass and username are correct")
elif username=="Bharat" and password=="ani123":
    print("correct username but wrong password")
else:
    print("wrong username")

#10)
Pin=int(input("Enter pin:"))
Acc_balance=float(input("Enter balance:"))
Withdrawl=int(input("Enter withdrawl amount:"))
if Pin==12345:
    pass
    if Withdrawl>=2000:
        pass
    else:
        print("please enter correct pin")
        if Acc_balance>=10000:
            print("ACCESS GRANTED")
else:
    print("Incorrect info")

#11)
Name=input("Enter nameof student:")
phy=int(input("Enter physics marks:"))
chem=int(input("Enter chemistry marks:"))
maths=int(input("Enter maths marks:"))
python=int(input("Enter python marks:"))
Marks=phy+chem+maths+python
print("Total marks are",Marks)
print("percentage is",Marks/400*100)
if Marks<100>=90:
    print("grade A+")
    print("Distinction")
if Marks<89>=80:
    print("garde A")
    print("Distinction")
if Marks<79>=70:
    print("grade B")
    print("Distinction")
if Marks<69>=60:
    print("Grade C")
if Marks<59>=50:
    print("grade D")
else:
    print("Fail")




