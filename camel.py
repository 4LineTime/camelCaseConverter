def camelcase(sentence):
    """ Convert sentence to camelCase, for example, "Display all books" 
    is converted to "displayAllBooks" """
    title_case = sentence.title() # Uppercase first letter of each word
    upper_camel_cased = title_case.replace(' ', '') # remove spaces 
    # Lowercase first letter, join with rest of string 
    # Slices don't produce index out of bounds errors. 
# So this still works on empty strings, strings of length 1
return upper_camel_cased[0:1].lower() + upper_camel_cased[1:] 
def main():
sentence = input('Enter your sentence: ')
output = camelcase(sentence)
print(output)
if __name__ == '__main__':
main()


Create branch
•
Commit any changes before making a branch
Type this to create a branch
git branch banner
And then check out that branch
git checkout banner
You can see a list of branches, and which one is 
currently checked out, with 
git branch
OR create branch and check it 
out, all in one command: 
git checkout -b banner


Add the banner 
feature
def camelcase(sentence):
""" Convert sentence to camelCase, for example, "Display all books" 
is converted to "displayAllBooks" """
title_case = sentence.title() # Uppercase first letter of each word
upper_camel_cased = title_case.replace(' ', '') # remove spaces 
# Lowercase first letter, join 
with rest of string 
# Slices don't produce index out of bounds errors. 
# So this still works on empty strings, strings of length 1
return upper_camel_cased[0:1].lower() + upper_camel_cased[1:] 
def display_banner():
""" Display program name in banner """
msg = 'AWSOME camelCaseGenerator PROGRAM'
stars = '*' * len(msg)
print(f'\n {stars} \n {msg} \n {stars}\n') 
def main():
display_banner()
sentence = input('Enter your sentence: ')
output = camelcase(sentence)
print(output)
if __name__ == '__main__':
main()

































