'''

Take three lowercase letters and print out binary.
Your input variable will contain a string of three lowercase letters. From this, you'll need to convert it to binary and print out the 24 number representation of those letters in binary.

Sample Test Case

Letter
value1 abc
output 011000010110001001100011

'''


value1 = input()
print(''.join('{0:08b}'.format(ord(x), 'b') for x in value1))
