import pandas as pd

question_8_dictionary = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

#Making a new variable as a dataframe of the question_8_dictionary
question_8_dictionary = pd.DataFrame(question_8_dictionary)

question_8_dictionary["D"] = [25, 50, 75, 100]

print(question_8_dictionary)
