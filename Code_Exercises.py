''' Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
exemple: create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns (123) 456-7890 '''
def create_phone_number(n):
   # we use slicing n
   separator_one = n[:3]
   separator_two = n[3:6]
   separator_three = n[6:]
   return f'({separator_one}) {separator_two}-{separator_three}'

print(create_phone_number('1234567890'))
# --------------------------------------------------------------------------------------------------------
''' Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value 
next to each other and preserving the original order of elements. exemple: ('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D'] '''
def unique_in_order(iterable):
    # save in a list
    chars = []
    # iterate
    for i in range(len(iterable)):
        if iterable[i] != iterable[i-1]:
            chars.append(iterable[i])
    return chars

print(unique_in_order('ABBCcAD'))
# --------------------------------------------------------------------------------------------------------
'''The examples below show you how to write function accum:
Examples: accum("abcd") -> "A-Bb-Ccc-Dddd" '''
def accum(text):
    result_list = list(text)
    for i in range(len(text)):
        # add to list multiply the characters lower and capitalize the first character
        result_list[i] = text[i].upper() + (text[i].lower() * i)
    return '-'.join(result_list)

print(accum('abcd'))
# --------------------------------------------------------------------------------------------------------
