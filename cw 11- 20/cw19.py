#Automorphic Number (Special Numbers Series #6)

# Test.describe("Basic tests")
# Test.assert_equals(automorphic(1),"Automorphic")
# Test.assert_equals(automorphic(3),"Not!!")
# Test.assert_equals(automorphic(6),"Automorphic")
# Test.assert_equals(automorphic(9),"Not!!")
# Test.assert_equals(automorphic(25),"Automorphic")
# Test.assert_equals(automorphic(53),"Not!!")
# Test.assert_equals(automorphic(76),"Automorphic")
# Test.assert_equals(automorphic(95),"Not!!")
# Test.assert_equals(automorphic(625),"Automorphic")
# Test.assert_equals(automorphic(225),"Not!!")
# print("<COMPLETEDIN::>")

#Done!
def automorphic(n):
    x = len(str(n))
    a = n**2
    b = "".join(str(a))
    c = "".join(str(n))
    print(c)
    
    if b[-x:] == c:
        return "Automorphic"
    else:
        return "Not!!"

# return "Automorphic" if str(n*n).endswith(str(n)) else "Not!!"      
    
print(automorphic(225))