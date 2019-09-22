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
