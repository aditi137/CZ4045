import pandas as pd
import os

inputSubdir = 'InputData'
question_ids = list(pd.read_csv(os.path.join(inputSubdir,'questions.csv'))['Id'])
print len(question_ids)
query = "select *\nfrom Posts\nwhere PostTypeId = 2\nand ParentId in ("
for i in range(len(question_ids)):
    query += str(question_ids[i])
    if i != len(question_ids)-1:
        query += ","
query += ")"
print query
