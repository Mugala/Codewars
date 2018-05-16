# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"
# Done!
def reverse_words(text):
    a =''.join(text).split(" ")
    c = []

    for i in a:
        b = i[::-1]   
        c.append(b)
    print(c)
    
    d = " ".join(c)
    return d 
    #  return ' '.join(s[::-1] for s in str.split(' '))
    
reverse_words("My name  is batman")