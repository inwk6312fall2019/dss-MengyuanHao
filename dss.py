#exercise 10-1
def nested_sum(list):
    total = 0
    for item in list:
        if isinstance(item,int):
           total = total + item
        elif isinstance(item,list):
           total = total + nested_sum(item)
    return total
    
 list = [[12],[13],[5,4]]
 print(nested_sum(list))
 
 #exercise 10-2
 def cumsum(t):
     sum = 0
     ans = []
     for n in t:
         sum = sum + n
         ans.append(sum)
     return ans
 
#exercise 10-3
def middle(t):
     return t[1:-1]
 
#exercise 10-4
def chop(t):
     del t[0]
     del t[-1]
     return t

#exercise 10-5
def is_sorted():
    i = 0
    while i < len(word) - 1:
          if word[i] < word[i+1]
             return True
          else:
             return False
    return t == sorted(t)
    
#exercise 10-6
def is_anagram(word1,word2):
    return sorted(word1) == sorted(word2)

#exercise 10-7
def has_duplicates(sl):
    for i in range(len(word)-1):
        if word[i] < len(word):
           return True
    return False

#exercise 10-8
def repeated(s):
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            return True
    return False
def random_birthday(r):
    ans = []
    for i in range(r):
        birthday = random.randint(1,365)
        ans.append(birthday)
    return ans
def count(student,num_same birthday):
    for i in range(num_same birthday):
        ans = random_birthday(student)
        if repeated(s):
            count = count + 1
    return count

#exercise 10-9
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

#exercise 10-10
def my_wordlist():
    my_wordlist = open('words.txt')
      for line in my_wordlist:
            word = line.strip()
            my_wordlist.append(word)
      return my_wordlist
def in_bisect(my_wordlist,word):
    i = in_bisect(my_wordlist,word)
    if m in i:
        return index[m]
    else:
        return None
    
#exercise 10-11
def reverse pair(my_wordlist,word):
    reverse word = word[::-1]
    for word in my_wordlist:
        if reverse pair(my_wordlist,word):
            print(word,reverse word)

#exercise 10-12
def interlock(wordlist,word):
    for w in range(n):
        interlock = word[w::n]
         if not in_bisect(my_wordlist,interlock):
                return False
    return True

#exercise 11-1
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

#exercise 11-2
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].setdefault([],val).append(key)
     return inverse

#exercise 11-3
def ackermann(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ackermann(m-1,1)
    else:
        return ackermann(m-1, ackermann(m, n-1))
return ackermann(m, n)

#exerrcise 11-4
def has_duplicates(s):
    dict = {}
    for i in s:
        if i in dict:
            return True
        d[x+1]
    return False

#exercise 11-5
def rotate_letter(l,n):
    if l.isupper():
        start = ord('A')
    elif l.islower():
        start = ord('a')
    else: 
        start = ord(l)
l_char = ord(l)
diff = start + ((l_char_start) + n) % 26
return char(diff)

def rotate_word(word,n):
    new_word = " "
    for letter in word:
        new_letter = rotate_letter(l,n)
        new_word += new_letter
return new_word

#exercise 12-1
def most_frequenr(f):
    histogram = word list
    ans = []
    for char in histogram:
        if char[i+1] < char[i]
           return True
        ans.append()
    return False

#exercise 12-2
def is_anagrams(word):
    ans = []
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i = i + 1
        j = j - 1
    return True
return ans.append(word)

#exercise 12-3
def metathesis_pair():
