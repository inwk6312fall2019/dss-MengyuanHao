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
