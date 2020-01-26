'''

Your input variable will contain a string of invalid JSON. However, each invalid JSON string received can be fixed by making one or more single character changes. Only three possible things may be wrong with the JSON string: 1) missing leading or trailing brace, 2) unquoted JSON string value, 3) missing comma between properties.

Sample Test Cases

Single Problem
value1 {"name":"em"
output {"name":"em"}

Multiple Problems
value1 "name":"em
output {"name":"em"}

'''

value1 = input()
value1 = value1.replace(" ", "")

str_start = False
full_pair = False
half_pair = False

if value1[0] != '{':
    value1 = '{' + value1

if value1[len(value1)-1] != '}':
    value1 = value1 + '}'

if len(value1) > 2:

    if value1[1] != '"':
        value1 = value1[0] + '"' + value1[1:]
        str_start = True
        full_pair = True

    elif value1[1] == '"':
        str_start = True
        full_pair = True

    if value1[len(value1)-2] != '"':
        value1 = value1[0:len(value1)-1] + '"' + value1[len(value1)-1:]

i = 2
while (i > 1) and (i < len(value1)):

    if (value1[i] == '"'):

        if (str_start == True) and (full_pair == True) and (half_pair == False):

            str_start = False
            if (value1[i + 1] != ':'):
                half_pair = True
                value1 = value1[:i + 1] + ':' + value1[i + 1:]


        elif (str_start == False) and (full_pair == True) and (half_pair == True):
            str_start = True

        elif (str_start == True) and (full_pair == True) and (half_pair == True):
            str_start = False
            half_pair = False

            if (value1[i + 1] != ',') and (value1[i + 1] != '}'):
                value1 = value1[:i + 1] + ',' + value1[i + 1:]

            full_pair = True

    elif (value1[i] == ','):
        full_pair = False

        if (value1[i-1] != '"'):
            value1 = value1[:i] + '"' + value1[i:]

        elif(value1[i+1] != '"'):
            value1 = value1[:i+1] + '"' + value1[i+1:]

    elif (value1[i] == ':'):
        half_pair = True

        if (value1[i-1] != '"'):
            value1 = value1[:i] + '"' + value1[i:]
            str_start = False

        elif (value1[i+1] != '"'):
            value1 = value1[:i+1] + '"' + value1[i+1:]
            str_start = False

    i += 1

print(value1)
