# def reverse_invert(lst):

#     a = lst
#     b = []
#     c = []

#     for i in a:
#         if i >= 10:
#             x = str(i)
#             y = x[::-1]
#             b.append(int(y))
#         elif i < 10:
#             b.append(i)

#     for i in b:
#     #     if i < 0:
#     #         x = i*-1
#     #         c.append(x)
#     #     elif i > 0:
#     #         x = -i 
#     #         c.append(x)
#     return -i if i > 0 else i
#     print(c)
    
# reverse_invert([2,3,10,23,47,86])

def square(num):
   squares=[]
   strnumber=str(num)
   strls=list(strnumber)
   for x in strls:
       y=int(x)
       mult=y*y
       squares.append(str(mult))
       final="".join(squares)
       int(final)
   return final
print (square(9119))

