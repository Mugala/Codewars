# In this Kata, you will be given a string and two indexes. Your task is to reverse the portion of that string between those two indices inclusive.

# solve("codewars",1,5) = "cawedors" -- elements at index 1 to 5 inclusive are "odewa". So we reverse them.
# solve("cODEWArs", 1,5) = "cAWEDOrs" -- to help visualize.
# Input will be lowercase and uppercase letters only.

# More examples in the test cases!

# Good luck!

# Done!
def solve(st,a,b):
    c = st[a:b+1]
    d = c[::-1]
    e = st[:a]
    f = st[b+1:]
    return e + d + f
#  return s[:a]+s[a:b+1][::-1]+s[b+1:]

solve("Mugala",1,4)