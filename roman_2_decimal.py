'''

Take a roman numeral(<1000 in value) and print its corresponding value in the decimal system of numbers.
Your input variable will contain a roman numeral less than 1000 in value. Print the corresponding value of the roman numeral in the decimal system of numbers.

Sample Test Cases

Small Roman Numeral
value1 VI
output 6

Large Roman Numeral
value1 CDVII
output 407

'''



value1 = input()

rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


total = 0
i = 0
while (i < len(value1)):
    if (i + 1) >= len(value1):
        total += rom_val[value1[i]]
        i += 1
    else:
        if rom_val[value1[i]] >= rom_val[value1[i+1]]:
            total += rom_val[value1[i]]
            i += 1
        else:
            total = total + rom_val[value1[i+1]] - rom_val[value1[i]]
            i += 2

print(total)