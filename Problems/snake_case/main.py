word = input()

for letter in word:
    if letter.isupper():
        word = word.replace(letter, "_" + letter.lower())

print(word)

# string = input()

# for letter in string:
#     if letter.isupper():
#         string = string.replace(letter, "_" + letter.lower())
#
# print(string)
