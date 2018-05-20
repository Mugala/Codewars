# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b.

# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(a, b):
    c =[]
    if len(b) ==0:
        return a
    else:
        for i in a:
            for n in b:
                if i != n:
                    c.append(i)
        print(c)
        d = set(c)
        print(d)

array_diff([-7, -6, 5, 5, 10, 2, 4, -2, -8, -14, 16, -1, 3, 19, 13, 0, 10, -10, 11, -12],[-18, -15, 12])
#[-7, -6, 5, 5, 10, 2, 4, -2, -8, -14, 16, -1, 3, 19, 13, 0, 10, -10, 11, -12]