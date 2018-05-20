def divisors(integer):
    a = []
    for i in range(2,integer):
        if integer % i == 0:
            print(i)
            b = a.append(i)
            print(b)    
divisors(12)