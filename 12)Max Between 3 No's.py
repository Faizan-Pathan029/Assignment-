def Max():
    A=int(input("Enter the No1:"))
    B=int(input("Enter the No2:"))
    C=int(input("Enter the No3:"))
    if(A>B) and (A>C):
        print("Max number is:",A)
    elif(A<B) and (C<B):
        print("Max number is:",B)
    else:
        print("Max number is:",C)
    
