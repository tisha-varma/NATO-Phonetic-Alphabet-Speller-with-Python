student_score = {
    "student": ['Angela', 'James', 'lily'],
    "score": [90, 80, 81]
}

# LOOPING THROUGH DICT
"""for (key, value ) in student_score.items():
    print(value)
"""
# Dataframe

import pandas

student_data_frame = pandas.DataFrame(student_score)
"""print(student_data_frame)"""

# LOOPING THROUGH A DATAFRAME Using same method as previous
"""for (key, values) in student_data_frame.items():
    print(values)
"""
# LOOPING THROUGH A DATAFRAME Using inbuilt loop : iter rows
for (index, row) in student_data_frame.iterrows():
    """print(index)
    print(row)"""
"""
    print(row.student)
    print(row.score)"""

"""
    if row.student == "Angela":
        print(row)
        """