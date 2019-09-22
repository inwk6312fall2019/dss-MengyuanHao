def myfile():
    myfile = open('words.txt')
    mydict = {}
    for word in myfile:
        word = word.strip()
        for char in word:
            if char not in mydict:
                mydict[char] = 1
            else:
                mydict[char] = mydict[char] + 1
print(mydict)
