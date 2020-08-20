'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word, count=0):
    # base
    if len(word) < 2:
        return count
    # recursive 
    for i, letter in enumerate(word):
        print(word, 'i', i, 'count', count)
        if i < len(word)-1 and letter == "t" and word[i+1] == "h":
            print('in if')
            count += 1
        return count_th(word[i+1:], count)


word1 = "abcthefthghith"
count1 = count_th(word1)
print(3, count1)

word2 = "thhtthht"
count2 = count_th(word2)
print(2, count2)

word3 = "THtHThth"
count3 = count_th(word3)
print(1, count3)

