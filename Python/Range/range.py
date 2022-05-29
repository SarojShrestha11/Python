numbers = list(range(10))
print(numbers)

#range with arguments
num = list(range(3,8))
print(num)

print(range(20) == range(0,20))

#using steps to determine interval
Number = list(range(3,20,5))
print(Number)

#going backwards
Numbers = list(range(100, 0, -9))
print(Numbers)

#using for loops with range
for i in range(5):
    print("Hello World!")
    
#printing the even values only
for i in range(0, 20, 2):
    print(i)