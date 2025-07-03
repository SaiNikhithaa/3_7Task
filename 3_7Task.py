# res={}
# for x in range(1,10):
#     if x%2==0:
#         res.setdefault("even",[]).append(x)
#     else:
#         res.setdefault("odd",[]).append(x)
# print(res)
#Invert a dictionary with list values (group keys by their values)
#Input:
#d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
#Output:
#{1: ['a', 'c'], 2: ['b'], 3: ['d']}
d={'a':1,"b":2,"c": 1,"d":3}
res={}
for key,value in d.items():
    res.setdefault(value,[]).append(key)
print(res)
#Find Max and Min Value in Dictionary
#Input:
#d = {'a': 10, 'b': 5, 'c': 15}
#Output:
#Max Value → 15
#Min Value → 5
d = {'a': 10, 'b': 5, 'c': 15}
max_value=max(d, key=d.get)
min_value=min(d, key=d.get)
print("max value",max_value,"->",d[max_value])
print("min value",min_value,"->",d[min_value])
#Create a dictionary using dictionary comprehension for the given list of numbers,
#where:
#• Each number is a key.
#•
#The value is "prime" if the number is prime.
#•
#The value is "notprime" if the number is not prime.
# Output: {2: 'prime', 3: 'prime', 4: 'notprime', 5: 'prime', 6: 'notprime'}
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
numbers=[1,2,3,4,5,6,7,8]
result = {n: 'prime' if is_prime(n) else 'notprime' for n in numbers}
print(result)
#Create a dictionary from a list of words, keys as words, values as word lengths, but
#only for words longer than 3 characters
# List: ["hi", "hello", "world", "is", "great"]
llist=["hi", "hello", "world", "is", "great"]
result={x:len(x) for x in llist if len(x)>3}
print(result)
#Create a dictionary with uppercase letters as keys and their ASCII values as values use
#dict comprehension .
#Input: letters = ['a', 'b', 'c']
#Expected Output:
#{'A': 65, 'B': 66, 'C': 67}
letter=['a','b','c','d']
final={x.upper(): ord(x.upper()) for x in letter}
print(final)
#. Explain about setdefault function in dictionary data type ?
"""setdefault() is used to get the value of a key, and if the key doesn't exist, it adds the key with a default value.
Syntax: dict.setdefault(key, default_value)"""
#7. Difference between d[key] and d.get(key)?
"""d[key] returns the value for the key but if key was not found then it raises a keyerror
d.get(key) returns the value for the keys but if the value was not found then it give output as None"""
#8. What is the difference between Shallow Copy and Deep Copy in Python? Explain with
#examples.
"""Shallow Copy:
Copies the outer object.

But inner objects are shared (same memory).

 Deep Copy:
Copies everything recursively — both outer and inner objects.

Changes to nested data do not affect the original."""