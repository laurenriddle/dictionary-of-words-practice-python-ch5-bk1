"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

word_definitions["Awesome"] = "The feeling of students when they are learning Python"
word_definitions["Good"] = "To be desired or approved of."
word_definitions["Okay"] = "Used to express assent, agreement, or acceptance."
# print(word_definitions)

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
# print(word_definitions["Good"])
# print(word_definitions["Awesome"])



"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

words = word_definitions.items()
for word in words:
    print(f"The definition of {word[0]} is { word[1]}")