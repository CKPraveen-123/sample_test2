# Defining the function
def add_numbers(*args):
    sum = 0
    for each_number in args:
        sum = sum + each_number
    print(f'sum of the numbers is {sum}')

