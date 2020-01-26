'''

Take a string of numbers and output the one which appears the most.
Your input variable will be a string of many numbers. You'll need to print out the number which appears the most times in that string.

Sample Test Cases

String of numbers
value1 08989082882348823838
output 8

'''


from collections import Counter
str = input()
print (str)
#sorted_str = sorted(str)
print(Counter(str).most_common(1)[0][0])