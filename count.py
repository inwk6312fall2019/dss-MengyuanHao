def count(word, letter):
	""" This takes in the var word which is the word you want search in
 and a var letter for which this returns the number of instances """
  
    count = 0

for char in word:
    if char == letter:
    count = count + 1
return count
print (count("banana","b"))
