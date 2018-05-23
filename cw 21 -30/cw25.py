from math import floor
def get_average(marks):
    # raise NotImplementedError("TODO: get_average")
    print(marks)
    a = 0
    b = len(marks)
    for i in marks:
        a +=i
    c = a/b
    print(floor(c)) 
get_average([1,2,3,4,5,6,7,8,9,10])


# def get_average(marks):
#     return sum(marks) / len(marks)