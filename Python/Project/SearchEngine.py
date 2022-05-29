def search(have,need):
    if need in have:
        return "Word Found"
    else:
        return "Word Not Found"
    
print("Enter the text:")
text = input()
print("Enter the word you want to search:")
word = input()

print(search(text,word))
    