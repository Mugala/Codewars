# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
    a =''.join(text).split(" ")
    c = []

    for i in a:
        b = i[::-1]   
        c.append(b)
    print(c)
    
    d = " ".join(c)
    return d 
    
reverse_words("My name  is batman")