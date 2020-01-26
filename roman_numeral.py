'''

Decimal to roman number conversion

'''



value1 = int(input())

val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
i = 0
roman = ''
while value1 > 0:
    for rem in range(value1//val[i]):
        value1 -= val[i]
        roman += syb[i]
    i += 1

print(roman)