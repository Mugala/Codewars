def palindrome_chain_length(n):
  print(n)
  x = ''
  a = 0
  while a > 0:
    a = int(str(n)[::-1]) + n
    n = a 
    x = str(a)
    if x == x[::-1]:
        break
    print(x)

palindrome_chain_length(87)