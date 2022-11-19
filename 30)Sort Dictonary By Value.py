A={82:"Name",99:"ram",2:"dictionary",9:"Abhi"}
sorted_values = sorted(A.values()) 
sorted_dict = {}

for i in sorted_values:
    for k in A.keys():
        if A[k] == i:
            sorted_dict[k] = A[k]

print(sorted_dict)
