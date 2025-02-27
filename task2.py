#WRITE A PROGRAMME TO FIND GREATEST OF NUMBERS
num1= int(input("enter first number"))
num2= int(input("enter second number"))
num3= int(input("enter third number"))

if num1>num2 and num1>num3:
    print("first number is greater number")
elif num2>num1 and num2>num3:
    print("second number is greater number")
elif num3>num1 and num3>num2:
    print("third number is greater number")
else:
    print("all three are equal")
#================================================================    
#check year is leap or not
year=int(input("enter year"))
if  (year % 4==0 and year %100) !=0 or ( year%400==0 and year %100==0):
    print(f"{year} is leap year")
else:
    print(f"{year} is non leap year")
#==============================================================
    
#write the code to check grade based on marks
marks= int(input("enter the marks"))
if (marks>=85 and marks<=100):
    print("Grade A: Exellent marks ")
elif (marks>=70 and marks<=84):
    print('Grade B: good  marks')
elif (marks>=40 and marks<=69):
    print('Grade C: avearge  marks')
else:
    print("FAIL")
#==============================================================
    
#PROGRAME TO CHECK IF A TRIANGLE IS VALID OR NOT BASED ON GIVEN 3 SIDES OF LENGTH
A= int(input("enter the length of first side "))
B= int(input("enter the length of second side "))
C= int(input("enter the length of third side "))
if (A+B)>C and (B+C)>A and (C+A)>B:
    print("will form valid triangle")
else:
    print("it will not form valid triangle")
#==============================================================



    