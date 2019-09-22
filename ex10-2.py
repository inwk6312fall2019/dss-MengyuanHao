def cumsum(t):
     sum = 0
     ans = []
     for n in t:
         sum = sum + n
         ans.append(sum)
     return ans
