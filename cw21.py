# Your car is old, it breaks easily. The shock absorbers are gone and you think it can handle about 15 more bumps before it dies totally.

# Unfortunately for you, your drive is very bumpy! Given a string showing either flat road ("_") or bumps ("n"), work out if you make it home safely. 15 bumps or under, return "Woohoo!", over 15 bumps return "Car Dead".

# Done!!

def bumps(road):
    b =[]
    a =' '.join(road).split()
    for i in a:
        if i == "n":
            b.append(i)
    if len(b) >=15:
        print("Car Dead")
    else:
        print( "Woohoo!")
bumps("_nnnnnnn_n__n______nn__nn_nnn")

#return "Woohoo!" if road.count("n") <= 15 else "Car Dead"