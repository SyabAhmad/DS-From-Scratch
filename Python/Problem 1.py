# - Write a Python function that takes a sentence as input and returns the reversed words in the sentence. For example, if the input is "Hello World", the output should be "olleH dlroW".

print("Solution 1")
inputString = input("Enter String here to reverse: ")

inputString = inputString.split()
print(type(inputString))
words = [word[::-1] for word in inputString]

inputString = ' '.join(words)

print(inputString)