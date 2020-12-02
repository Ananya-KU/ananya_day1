#Write a Python program to check for a number at the end of a word/sentence.
import re
def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False

print(end_num('aef'))
print(end_num('abf6'))
