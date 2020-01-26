'''

Given a string with multiple words, return the longest word.
You'll get one input, a string with multiple words. Return the longest word in the string. If the input contains multiple words that are the largest length, return a string that contains all of the words in the same order they are provided. All returned strings should be lowercase and trimmed of whitespace.

Sample Test Cases

Regular
value1 run,barn,yellow,barracuda,shark,fish,swim
output barracuda

Same Size
value1 fishes,sam,gollum,sauron,frodo,balrog
output fishes,gollum,sauron,balrog

'''

value1 = input()
value1 = value1.replace(" ", "").lower()
print(value1)
str_list = sorted(value1.split(','),key=len, reverse=True)
max_len = len(str_list[0])
new_list = []
for str in str_list:
    if len(str) == max_len:
        new_list.append(str)
    else:
        break
print(*new_list,sep=',')
