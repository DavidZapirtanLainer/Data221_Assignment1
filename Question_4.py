from random import random #Import random to generate random

#Getting a random value for x, and a list of 20 random values between 0 and 1
list_of_random_values = [random() for i in range(20)]
random_value_x = random()


list_of_values_greater_than_x = []

#Creating a list to put all indices of the list that are equal to x
#By doing this we are able to call the zero index of this list to show the first index that matched x
indices_of_matching_values_to_x = []

#For loop to add all values equal to or greater than x into a list
for i in range(len(list_of_random_values)):
    if list_of_random_values[i] >= random_value_x:
        list_of_values_greater_than_x.append(list_of_random_values[i])
        if list_of_random_values[i] == random_value_x:
            indices_of_matching_values_to_x.append(i)

#Sorting the list from least to greatest
list_of_values_greater_than_x = sorted(list_of_values_greater_than_x)

print(f'''Values equal to or greater than x from our random generated numbers: 
{list_of_values_greater_than_x}''')


print(f"The value of x is: {random_value_x}")


if len(indices_of_matching_values_to_x) > 0:
    print(f"The first index of a number that matches x before sorting was: {indices_of_matching_values_to_x[0]}")
else:
    print("There were no values in the random list that were equal to x")
