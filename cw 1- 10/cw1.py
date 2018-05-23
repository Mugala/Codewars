# Some people just have a first name; some people have first and last names and some people have first, middle and last names.

# You task is to initialize the middle names (if there is any).

# Examples
# 'Jack Ryan'                   => 'Jack Ryan'
# 'Lois Mary Lane'              => 'Lois M. Lane'
# 'Dimitri'                     => 'Dimitri'
# 'Alice Betty Catherine Davis' => 'Alice B. C. Davis'

# Done!

def initialize_names(name):
    list_a = []

    list_a.append(name)
    list_a = name.split()

    a = list_a[0]
    b =list_a[-1]
    y = list_a[1:-1]

    if len(list_a) > 1:
        x = ' '.join(y)

        c = "" 
        for i in x.split():
            c += i[0] + "." + " "
            
        return a +" "+ c +b
    else:
        return a
print(initialize_names("Levi Mugala Luyari Brenda"))