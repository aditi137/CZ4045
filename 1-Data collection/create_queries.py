import pandas as pd

question_ids = list(pd.read_csv('questions.csv')['Id'])
print question_ids[0:5]
query = "select *\nfrom Posts\nwhere PostTypeId = 2\nand ParentId in ("
for i in range(len(question_ids)):
    query += str(question_ids[i])
    if i != len(question_ids)-1:
        query += ","
query += ")"
print query