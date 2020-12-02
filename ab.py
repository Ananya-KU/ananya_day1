#Write a Python program that matches a word containing 'ab'.
import re
def text_match(text):
        patterns = 'ab{1}?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ab"))
print(text_match("ada"))