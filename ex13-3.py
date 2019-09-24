hist = my_book
sort_hist = []
for word,count in hist.items():
    sort_hist.append((count,word))
    sort_hist.sort(reverse = True)
print(sort_hist[:20])
