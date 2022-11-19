def prime(a):
    for i in range (2,a) :
        if a % i == 0 :
            return "This is not prime number"
    return "Prime number"

a = int(input("Enter a number : "))
print(prime(a))

 
