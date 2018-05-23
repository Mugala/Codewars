# Generate random password

import string
import random

def gen_password(n, password):

    x =''.join(random.choice(password) for _ in range(n))

    print(x)

gen_password(8, string.ascii_letters + string.digits)