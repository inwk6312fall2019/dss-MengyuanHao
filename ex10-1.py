def nested_sum(list):
    total = 0
    for item in list:
        if isinstance(item,int):
           total = total + item
        elif isinstance(item,list):
           total = total + nested_sum(item)
    return total
