# Definition
# Balanced number is the number that The sum of all digits to the left of the middle digit(s) and the sum of all digits to the right of the middle digit(s) are equal.

# Task
# Given a number, Find if it is Balanced or not .

# Warm-up (Highly recommended)
# Playing With Numbers Series
# Notes
# If the number has an odd number of digits then there is only one middle digit, e.g. 92645 has middle digit 6; otherwise, there are two middle digits , e.g. 1301 has middle digits 3 and 0

# The middle digit(s) should not be considered when determining whether a number is balanced or not, e.g 413023 is a balanced number because the left sum and right sum are both 5.

# Number passed is always Positive .

# Return the result as String

# Input >> Output Examples
# 1- balancedNum (7) ==> return "Balanced"   .
# Explanation:
# Since , The sum of all digits to the left of the middle digit (0)

# and the sum of all digits to the right of the middle digit (0) are equal , then It's Balanced

# 2- balancedNum (295591) ==> return "Not Balanced" .
# Explanation:
# Since , The sum of all digits to the left of the middle digits (11)

# and the sum of all digits to the right of the middle digits (10) are equal , then It's Not Balanced

# Note : The middle digit(s) are 55 .

# 3- balancedNum (959) ==> return "Balanced"  .
# Explanation:
# Since , The sum of all digits to the left of the middle digits (9)

# and the sum of all digits to the right of the middle digits (9) are equal , then It's Balanced

# Note : The middle digit is 5 .

# 4- balancedNum (27102983) ==> return "Not Balanced"  .
# Explanation:
# Since , The sum of all digits to the left of the middle digits (10)

# and the sum of all digits to the right of the middle digits (20) are equal , then It's Not Balanced

# Note : The middle digit(s) are 02 .

# Playing with Numbers Series
# Playing With Lists/Arrays Series
# For More Enjoyable Katas
# ALL translations are welcomed
# Enjoy Learning !!
# Zizou

# Done!
def balanced_num(number):
    a = " ".join(str(number)).split()
    z = len(a)
    if z % 2 !=0:
        b = (z+1)//2
        c = a[:b-1]
        d = a[b:]
        f=g=0
        for i in c:
            f += int(i)
        for i in d:
            g += int(i)
        if f ==g:
            print("Balanced")
        else:
            print("Not Balanced")

    elif z % 2 ==0:
        z = len(a)
        b = z//2
        c = b+1
        d =a[:b-1]
        e =a[c:]
        f = g = 0
        for i in d:
            f +=int(i)
        for i in e:
            g +=int(i)
    if f == g:
        print("Special")
    else:
        print('not special')
    
balanced_num(4445444)


# def balancedNum(n):
#     s = str(n)
#     l = (len(s)-1)//2
#     same = len(s) < 3 or sum(map(int, s[:l])) == sum(map(int, s[-l:]))
#     return "Balanced" if same else "Not Balanced"

# balanced_num = balancedNum