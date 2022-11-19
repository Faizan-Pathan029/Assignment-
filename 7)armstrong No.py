n=int(input("Enter No"))
s=0
n1=n
while n>0:
    d=n%10
    s=s+d**3
    n=n1//10
if s==n1:
    print("no is arm")
else:
    print("no is not arm")
