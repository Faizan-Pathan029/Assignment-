num=int(input("Enter Number= "))
if num>1:
    for i in range(2,num):
         if (num%i)==0:
                print(num,"Number Is Not prime")
                break
    else:
        print(num,"Is prime")
        
