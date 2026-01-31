def list_of_strings_to_nested_dictionary(list_of_strings):
    #Empty dictionary created that will store all of the information later on
    string_information_dictionary = {}

    #Looping through the list of strings and getting their length, as well as
    # checking if it is even or odd and adding it to a dictionary
    for i in range(len(list_of_strings)):
        string_information_dictionary[list_of_strings[i]] = {}
        string_information_dictionary[list_of_strings[i]]["length"] = len(list_of_strings[i])


        if len(list_of_strings[i]) % 2 == 0:
            string_information_dictionary[list_of_strings[i]]["parity"] = "even"
        else:
            string_information_dictionary[list_of_strings[i]]["parity"] = "odd"

    return string_information_dictionary

list_of_strings_example = ["one", "two", "three", "four", "five"]

string_information_result = list_of_strings_to_nested_dictionary(list_of_strings_example)

#For loop to print out key, value pair by line
for key, item in string_information_result.items():
    print(key +":", item)


