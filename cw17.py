def min_max(lst):
    c =[]
    a = min(lst)
    c.append(a)
    b = max(lst)
    c.append(b)
    return c
# return [min(lst), max(lst)]
min_max([1,2,3,4,5])