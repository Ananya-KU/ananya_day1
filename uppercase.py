#Write a Python program to match a string that contains only uppercase letters
import re
def text_match(text):
        patterns = '^[A-Z]'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("the quick brown fox jumps over the lazy dog."))
print(text_match("PYTHON EXERCISES"))
