# None

#Numeric data types int,float, complex and boolean

num = 5
print("int type:",type(5)) # int type

a = 5.5
print("float type:",type(a)) # float type

c = 6 + 9j
print("complex type:",type(c)) # complex type

d = int(True)
print(d) 
print(" Boolean but give 1 as integer:",type(d))     # Boolean but give 1 as integer

e = bool(1)
print("Boolean type",type(e)) # Boolean type

ran = range(10)
print(ran) # printing the value 10

print(list(range(10))) # We are creating list it contains 1 to 10.

print("3 parameters:",list(range(0,13,3))) # value 0 to 11 with gap 3 

print("Range type:",type(range(0))) # range type