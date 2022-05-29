numbers = [0, 1, 2, 3, 4, 5, 6]
print(len(numbers))

Letters = ["a", "b", "c", "d", "e", "f"]
Letters += ["g"]
print(len(Letters))

#append-----add items to the last of the lists----
nums = [0, 1, 2, 3, 4, 5, 6]
nums.append(7)
print(nums)

#insert-----add items to the listed index of the lists---
words = ["Python", "fun"]
index = 1
words.insert(index,"is")
print(words)

letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters)
print(letters.index('b'))
print(letters.index('d'))
print(letters.index('f'))

print(max(letters))#returns the maximum item
print(min(letters))#returns the minimum item
print(letters.count('c'))# returns the count of how
#many items occurs in the list
letters.reverse()#reverse the list
print(letters)