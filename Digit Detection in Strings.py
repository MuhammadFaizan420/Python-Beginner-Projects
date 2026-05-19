input_string = "Python3"
contains_digit = False
for letter in input_string:
    if letter.isdigit():
        contains_digit = True
        break
print(f'the string {input_string} contains digits: {contains_digit} ')