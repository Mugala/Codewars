# Definition
# Disarium number is the number that The sum of its digits powered with their respective positions is equal to the number itself.

# Task
# Given a number, Find if it is Disarium or not .

# Warm-up (Highly recommended)
# Playing With Numbers Series
# Notes
# Number passed is always Positive .
# Return the result as String
# Input >> Output Examples
# 1- disariumNumber(89) ==> return "Disarium !!"
# Explanation:
# Since , 81 + 92 = 89 , thus output is "Disarium !!"
# 2- disariumNumber(564) ==> return "Not !!"
# Explanation:
# Since , 51 + 62 + 43 = 105 != 546 , thus output is "Not !!"

# Playing with Numbers Series
# Playing With Lists/Arrays Series
# For More Enjoyable Katas
# ALL translations are welcomed
# Enjoy Learning !!
# Zizou

# def disarium_number(number):
#     a = '   '.join(str(number)).split()
#     b = 0
#     for i in a:
#         x=a.index(i)+1
#         b += int(i)**x
#     print(b)
#     if b == number:
#         return "Disarium !!"
#     else:
#         return "Not !!"    

# print(disarium_number(1024))


# def total_string(string):
#     a=3
#     b=6
#     c=8
#     x=0
#     full=' '.join(string).split()

#     print(full)


def total_string(string):
    a=3
    b=6
    c=8
    x=0
    full=' '.join(string).split()

    print(full)


    for item in full:
        if item == 'a':
            x+=a
            print(x)

        if item =='b':

            return b

        if item == 'c':

            return c

        total= x + b + c



total_string('this is absolutely crazy')