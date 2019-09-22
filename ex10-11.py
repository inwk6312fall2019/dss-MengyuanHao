def reverse pair(my_wordlist,word):
    reverse word = word[::-1]
    for word in my_wordlist:
        if reverse pair(my_wordlist,word):
            print(word,reverse word)
