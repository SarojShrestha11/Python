#format() embed values in string, using placeholders
nums = [4, 5, 6, 7, 8, 9]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)
##################################################################
a = "{x}, {y}, {z}".format(x=1, y=2, z=3)
print(a)
###################################################################
#joins the list of strings with another string as a separator 
print(", ".join(["spam", "eggs", "ham"]))
#turns a string with a certain separator into a list
print("spam, eggs, ham".split(", "))

print("Hello Me".replace("Me", "World"))
print("This is a sentence.".startswith("This"))
print("This is a sentence.".endswith("sentence."))
print("This is a sentence.".upper())
print("This is a sentence.".lower())

