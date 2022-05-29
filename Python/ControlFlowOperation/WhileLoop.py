print("Enter 1 to start:")
i = int(input())
print('\n')
while i <= 5:
    print(i)
    i = i + 1
    
print("Finished.")
print("\n")

#Finding odd and even numbers in 10 digits.
x = 1
while x < 10:
    if x%2 == 0:
        print(str(x) + " is even.")
    else:
        print(str(x) + " is odd.")
    
    x += 1