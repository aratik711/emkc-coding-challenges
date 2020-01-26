'''

Given two strings of equal length, figure out if one is a scramble of the other.
Your input variable will contain two strings of equal length, separated by a comma. You have to check whether the second string is a permutation of the first string. Print "Yes" if it is, "No" if not.

Sample Test Case

Permutation
value1 brian,airbn
output Yes

'''

value1 = input()
#print(value1)
str1,str2=value1.split(",")
if sorted(str1) == sorted(str2):
    print("Yes")
else:
    print("No")