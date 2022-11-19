A=[2,3,5,4,4,4,4,5,5,6,9,8,7,3,2]
B=[]
for i in A:
   if i not in B:
       B.append(i)
print(B)
