"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
"""
# import pytest
from collections import OrderedDict
def no_duplicates(a_string):
    return  ''.join(sorted(set(a_string)));
print("***sorted and no duplicates:***")
print(no_duplicates("monty pythons flying circus"));
print("\n")
def reversed_words(a_string):
    l=list(a_string.split(" "))
    newl=[]
    for i in reversed(l):
        newl.append(i);
    return newl;
print("***in reverse:***");
print(reversed_words("monty pythons flying circus"))
print("\n")
def four_char_strings(a_string):
    l=[a_string[i:i+4] for i in range(0, len(a_string), 4)]
    return l
print("***string sliced by four***")
print(four_char_strings("monty pythons flying circus"));
# def test_no_duplicates():
#     s = 'monty pythons flying circus'
#     assert no_duplicates(s) == ' cfghilmnoprstuy'
#
#
# def test_reversed_words():
#     s = 'monty pythons flying circus'
#     assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']
#
#
# def test_four_char_strings():
#     s = 'monty pythons flying circus'
#     assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
#
# def main():
#     return pytest.main(__file__)
#
#
# if __name__ == '__main__':
#     main()