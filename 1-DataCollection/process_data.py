import os
import pandas
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
import re

nltk.download('punkt')
plt.style.use('ggplot')


def convert_html_to_text(row):
    body = row['Body']
    bs_obj = BeautifulSoup(body, "lxml")
    codeblocks = bs_obj.select('pre > code')
    for codeblock in codeblocks:
        codeblock.decompose()
    text = bs_obj.text
    text = re.sub(r'\n\n+', '\n', text)
    return text.strip()


def text_word_count(row):
    return len(word_tokenize(row['Text']))


def add_columns(dataframe):
    dataframe['Text'] = dataframe.apply(convert_html_to_text, axis=1)
    dataframe['Post length'] = dataframe.apply(text_word_count, axis=1)
    dataframe.drop('Body', axis=1, inplace=True)
    return dataframe

#### Main Program ####
inputSubdir = 'InputData'
outputSubdir = 'OutputData'
if not os.path.exists(outputSubdir):
    os.makedirs(outputSubdir)

questions = pandas.read_csv(os.path.join(inputSubdir, 'questions.csv'))
answers = pandas.read_csv(os.path.join(inputSubdir, 'answers.csv'))
questions['ParentId'] = questions['Id']

questions = add_columns(questions)
answers = add_columns(answers)
questions = questions.loc[questions['Post length'] > 0]
answers = answers.loc[answers['Post length'] > 0]
# print answers.info()

questions = questions.set_index('ParentId')
questions_with_answer = answers.groupby('ParentId').count()['Id']
questions = questions.loc[questions_with_answer.index].dropna()  # select only questions with available answers
questions['AnswerCount'] = questions_with_answer  # update AnswerCount with number of available answers

# print questions.info()

### Statistics ###

# questions and answers count
number_of_questions = questions.shape[0]
number_of_answers = answers.shape[0]

print '*** Dataset Statistics ***'
print '1. Number of questions:', number_of_questions
print '2. Number of answers:', number_of_answers

# number of answers for each question count

answers_count = pandas.DataFrame(columns=['count'])
answers_count['count'] = questions_with_answer
answers_count = answers_count.reset_index()
answers_count = answers_count.groupby('count').count().reset_index()
answers_count.columns = ['Number of answers in a question', 'Number of questions']
answers_count['percentage'] = answers_count['Number of questions'] * 100 / number_of_questions
print '3. Distribution of numbers of answers in a question...'
answers_count.to_csv(os.path.join(outputSubdir, 'answers_count.csv'), index=False)
answers_count.plot.bar(x='Number of answers in a question', y='Number of questions')
plt.xlabel('answers count')
plt.ylabel('number of questions')
plt.savefig(os.path.join(outputSubdir, 'answer_count_hist.png'))
plt.show()

# post word count
questions = questions.reset_index()
posts = pandas.concat([questions, answers]).sort_values('ParentId')[
    ['ParentId', 'Id', 'PostTypeId', 'Text', 'Post length']].reset_index(drop=True)

posts_length = posts.groupby('Post length').count()[['Id']]
posts_length.columns = ['Number of posts']
posts_length = posts_length.reset_index()
posts_length.to_csv(os.path.join(outputSubdir, 'word_count.csv'), encoding='utf-8', index=False)

posts.hist('Post length', bins=range(0, posts_length['Post length'].max()+1, 20), edgecolor='black')
plt.xlabel('post length')
plt.ylabel('number of posts')
plt.savefig(os.path.join(outputSubdir, 'word_count_hist.png'))
plt.show()

posts.to_csv(os.path.join(outputSubdir, 'posts.csv'), index=False, encoding='utf-8')


