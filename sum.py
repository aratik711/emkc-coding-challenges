'''

Take a string of comma separated numbers and print out the sum.

Your input variable could contain a list of integer values. Regardless of value, you'll need to print out the sum of the list.

Sample Test Cases

Short list
value1 2,5,1
output 8

Long list
value1 3,9,10,5,2,7,9,2
output 47

'''



value1 = input()
print(value1)
arr = list(map(int,(value1.split(','))))
print(sum(arr))