'''

Given a string with multiple words, find the most common character.
You will be given a string and your job is to find the most common character in that string. If there are two characters which appear the same amount of times and are the largest amount, you should output both separated by a comma in the order they first appeared.

Sample Test Cases

Short phrase
value1 A test case
output t,e,s

Long phrase
value1 The way this mode works is by looking for the mode of the characters of any given string
output o

'''
from collections import Counter


value1 = input()
value1 = value1.replace(" ","")

# Returns the first items value in the list of tuples (i.e) the largest number
# from Counter().most_common()
largest_count = Counter(value1).most_common()[0][1]

# If the tuples value is equal to the largest value, append it to the list
most_common_list = [ x
                         for x, y in Counter(value1).items() if y == largest_count]

print(*most_common_list,sep=",")
