import pandas as pd
from bs4 import BeautifulSoup


def convert_html_to_text(row):
    bs_obj = BeautifulSoup(row['Body'], "lxml")
    return bs_obj.text

questions = pd.read_csv('questions.csv')
answers = pd.read_csv('answers.csv')
questions['ParentId'] = questions['Id']

questions = questions.set_index('ParentId')
questions_with_answer = answers.groupby('ParentId').count()['Id']
questions = questions.loc[questions_with_answer.index].dropna()  # select only questions with available answers
questions['AnswerCount'] = questions_with_answer  # update AnswerCount with number of available answers

### Statistics ###

# questions and answers count
number_of_questions = questions.shape[0]
number_of_answers = answers.shape[0]

print '*** Dataset Statistics ***'
print '1. Number of questions:', number_of_questions
print '2. Number of answers:', number_of_answers

# number of answers for each question count

answers_count = pd.DataFrame(columns=['count'])
answers_count['count'] = questions_with_answer
answers_count = answers_count.reset_index()
answers_count = answers_count.groupby('count').count().reset_index()
answers_count.columns = ['Number of answers in a question', 'Number of questions']
answers_count['percentage'] = answers_count['Number of questions'] * 100 / number_of_questions
print '3. Distribution of numbers of answers in a question'
print answers_count

# post word count
questions = questions.reset_index()
posts = pd.concat([questions, answers]).sort_values('ParentId')[['ParentId', 'Id', 'PostTypeId', 'Body']].reset_index(drop=True)
posts['Text'] = posts.apply(convert_html_to_text, axis=1)
posts.drop('Body', axis=1, inplace=True)
posts.to_csv('posts.csv', index=False, encoding='utf-8')






