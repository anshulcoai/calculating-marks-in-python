#write a program to read 5 subject marks from user. Calculate the total marks, percentage and check result.
a=int(input("Enter the marks of maths :"))
b=int(input("Enter the marks of science :"))
c=int(input("Enter the marks of sociology :"))
d=int(input("Enter the marks of psychology :"))
e=int(input("Enter the marks of history :"))

t=a+b+c+d+e
p=t/5

print("Total Marks :",t)
print("Percentage is :",p,"%")

if p<40:
    print("This Student is Fail")
else:
    print("This Student is passed ")

