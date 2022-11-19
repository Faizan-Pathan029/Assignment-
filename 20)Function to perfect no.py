def num_perfect(num):  
    sum_n = 0  
    for i in range(1, num):  
        if num % i == 0:  
            sum_n=sum_n+i  
    return sum_n == num  
print(num_perfect(26))  
