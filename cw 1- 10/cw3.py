# Welcome. In this kata, you are asked to square every digit of a number.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# Note: The function accepts an integer and returns an integer

# return int(''.join(str(int(d)**2) for d in str(num))

#Done!



def square_digits(num):

    x = [int(i) for i in str(num)] #list comprehension
    result =""
    for n in x:
        t = str(n**2)

        result +=t

    return int(result)

print(square_digits(9119))

# def square_digits(num):
#     a = []
#     x = str(num)

#     x = ' '.join(x)

#     b = x.split()


#     for i in b:
#         c = int(i)**2
#         a.append(str(c))
#     d = ""
#     for i in a:
#         d +=i
#         e = int(d)

#     return e
    

# print(square_digits(9119))