import string
PUNCT = string.punctuation
def read_word(file):
   my_file = open(file)
   histogram = dict()
      for line in my_file:
          word = word.split(PUNCT).lower()
          histogram[word] = histogram.get(word, 0) + 1
return histogram
