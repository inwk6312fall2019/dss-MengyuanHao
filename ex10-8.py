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
