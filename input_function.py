# Input the numbers to add


number_list = (input('enter the numbers you want to add.Give numbers type <spacebar> and then give next')).split()
float_list = list(map(float, number_list))
print(f'The numbers you entered are {float_list}')
