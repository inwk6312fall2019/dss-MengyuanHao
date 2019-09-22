def my_wordlist():
    ans = []
    my_wordlist = open('words.txt')
    for line in my_wordlist:
        word = line.strip()
        ans.append(word)
        return ans
print(word)

def my_wordlist():
    ans = []
    my_wordlist = open('words.txt')
    for line in my_wordlist:
        word = line.strip()
        ans = ans + [word]
        return ans
print(word)
