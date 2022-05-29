def my_function():
    print("Spam")
    print("eggs")
    print("ham")
    
my_function()

def hello():
    print("Hello world!")
    
hello()
hello()
hello()

#Using functions with arguments
def arguments(word):
    print(word + "!")
arguments("Hello")
arguments("World")
arguments("spam")

def sum(x,y):
    print(x+y)
sum(1,2)

#Returning from functions
def greatest(x,y):
    if x >= y:
        return x
    else:
        return y
    
print(max(4,7))
z = max(8,4)
print(z)