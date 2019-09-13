'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
count = 0

def count_th(word):

    # TBC
    # return word.count('th')
    global count

    if not word:
        return 0
    elif len(word) > 1:
        if word[0] == "t" and word[1] == "h":
            count += 1
            return count_th(word[1:])
        else:
            return count_th(word[1:])
    final_count = count
    count = 0
    return final_count


