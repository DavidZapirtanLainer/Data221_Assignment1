def compute_x_to_the_power_of_y(x, y): #Simple function that takes an x and y, and returns x to the y
    return x ** y

example_list_of_pairs_x_y = [[5,2],[3,-1],[4,3],[2,0]]

#List created for valid results
valid_exponent_results = []

#Looping through all the values, only allowing positive numbers for the exponent,
#Then using argument unpacking to turn the nested list into a tuple to pass into compute_x_to_the_power_of_y
for i in range(len(example_list_of_pairs_x_y)):
    if example_list_of_pairs_x_y[i][1] >= 0:
        exponent_value = compute_x_to_the_power_of_y(*example_list_of_pairs_x_y[i])
        valid_exponent_results.append(exponent_value)
    else:
        pass

print(valid_exponent_results)