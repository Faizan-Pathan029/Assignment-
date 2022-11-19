""" we cannot change the elements in a tuple. It means that we cannot
delete or remove items from a tuple.
Deleting a tuple entirely, however, is possible using the keyword del """
a = (1, 2, 3, 4, 5)
b = a[:2] + a[3:]
print(b)
