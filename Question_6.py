def list_to_element_information_dictionary(list_of_numbers):

    #Creating an empty dictionary to display the list element information later on.
    list_value_information_dictionary = {}

    #Sorting the list of numbers before doing any operations so the dictionary is sorted at the end
    list_of_numbers = sorted(list_of_numbers)

    #Using the for loop to go through all the values in the original list, get the necessary info, and adding it into the dictionary.
    for number in list_of_numbers:
        number_of_elements_equal_to_or_less = 0

        #Passing if the number has already as been placed as a key.
        if number in list_value_information_dictionary.keys():
            pass

        #For loop to get number of values that are equal to or less than i
        for element in list_of_numbers:
            if element <= number:
                number_of_elements_equal_to_or_less += 1

        percentage_of_elements_equal_to_or_less = (number_of_elements_equal_to_or_less/len(list_of_numbers)) * 100

        #Rounding to two decimal places for aesthetic purposes
        list_value_information_dictionary[number] = f" {round(percentage_of_elements_equal_to_or_less,2)}%"


    return list_value_information_dictionary


test_list_for_function = [3, 1, 2, 3, 4, 2]
print(list_to_element_information_dictionary(test_list_for_function))





