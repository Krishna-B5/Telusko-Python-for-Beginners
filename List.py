# List mutable (You can replace the list values after assigning also)
# It's a collection of different data types

nums = [1,3,5,7,9,11]
print(nums)
length = len(nums)
print("\nLength of the string is :",length)
print("\nFirst value of list :",nums[0])
print("\nLast value of list :",nums[5])
print("\nSecond to last value of list :",nums[1:])

values = ["Krishna",30.2,1990] # Collection of different data types.
print("\n\n")
print(values)
print("\n\n list within list")
twolist = [nums,values]
print(twolist)
# print("Insert only one value at the any positions of list",twolist.insert(0,5,55)) syntax error
print("\n\n")
lt = [1,2,3,4,5,6,7,8,9]

# Perforning some list operations
print(lt)
print("Append Add the values at the end of list",lt.append(10))
print(lt)
print("Insert only one value at the any positions of list",lt.insert(5,55))
print(lt)
print("Extend insert multiple values at the end of list",lt.extend([6,66,7,77]))
print(lt)
print("Remove the values from the list",lt.remove(6))
print(lt)
print("POP is remove the elements by index",lt.pop(5))
print(lt)
print("POP is remove the last element without index",lt.pop())
print(lt)
print("Minimun",min(lt))
print("Maximun",max(lt))
print("sort",lt.sort(reverse=True)) # decending order
print(lt)
print("sort",lt.sort()) # Ascending order
print(lt)
print("Sum of list",sum(lt))
# print("Deleting the value from list",del lt[1:3])
print("Clearing the values",lt.clear())
print(lt)