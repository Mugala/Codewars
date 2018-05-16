# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
    # a =''.join(text).split()
    # c = []

    # for i in a:
    #     b = i[::-1]   
    #     c.append(b)
    # print(c)
    
    # d = " ".join(c)
    # print(d)   
    # x = len(text)
    # print(x)
    # y = len(d)
    # print(y)

    words = text.split("")
    rev_words = []
    for word in words:
        rev_words.append(word[::-1])
    reverse_s = "".join(rev_words)
    return reverse_s


reverse_words("My name  is batman")