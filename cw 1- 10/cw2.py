# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

# Example:

# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0
# Notes:

# The number can be negative already, in which case no change is required.
# Zero (0) can't be negative, see examples above.
#Done!

def make_negative(number):
    # if number == 0:
    #     return 0
    # elif number < 0:
    #     return number
    # else:
    #     return number * -1


    return -number if number > 0 else number

print(make_negative(-9))
