'''

Take a sentence/phrase in pig latin, translate it to English.

Your input variable will contain a sentence/phrase in pig latin. Your job is to translate it to english. You add "yay" if the word starts with a vowel. Otherwise move the starting consonant sequence (w, wr, sch, ...) to the end of the word and add "ay" plus a dash.

Sample Test Cases

Short phrase
value1 ayay imple-say est-tay ase-cay
output a simple test case

Long phrase
value1 ig-pay atin-lay isyay usedyay inyay ools-schay o-tay each-tay anguage-lay onstructs-cay
output pig latin is used in schools to teach language constructs

'''


value1 = input()

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
eng_sent = []
words = value1.split()
for word in words:

    if ('-' in word):
        arr = word.split('-')
        if arr[1][0] not in vowels:
            eng_sent.append(arr[1][:-2] + arr[0])
        else:
            eng_sent.append(word)
    elif word[0] in vowels:
        eng_sent.append(word[:-3])

print(*eng_sent, sep=' ')
