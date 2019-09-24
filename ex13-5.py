def choose_from_hist():
    hist = histogram()
    freqs = []
    for count,word in sort_hist:
        freqs.append(count)
    return [count,word]
