# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# double_char("String") ==> "SSttrriinngg"

# double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"

# double_char("1234!_ ") ==> "11223344!!__  "

#Done!

def double_char(s):
    b ="".join(s)
    print(b)

    c =""
    for i in b:
        c += 2*i
    print(c)
double_char("Levi Mugala")


    # return ''.join(c * 2 for c in s)

