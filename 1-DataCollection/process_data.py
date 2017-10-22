import os
import pandas
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
plt.style.use('ggplot')

def convert_html_to_text(row):
    bs_obj = BeautifulSoup(row['Body'], "lxml")
    return bs_obj.text

def text_word_count(row):
    return len(word_tokenize(row['Text']))

inputSubdir = 'InputData'
outputSubdir = 'OutputData'
if not os.path.exists(outputSubdir):
	os.makedirs(outputSubdir)

questions = pandas.read_csv(os.path.join(inputSubdir, 'questions.csv'))
answers = pandas.read_csv(os.path.join(inputSubdir, 'answers.csv'))
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

answers_count = pandas.DataFrame(columns=['count'])
answers_count['count'] = questions_with_answer
answers_count = answers_count.reset_index()
answers_count = answers_count.groupby('count').count().reset_index()
answers_count.columns = ['Number of answers in a question', 'Number of questions']
answers_count['percentage'] = answers_count['Number of questions'] * 100 / number_of_questions
print '3. Distribution of numbers of answers in a question'
print answers_count

# post word count
questions = questions.reset_index()
posts = pandas.concat([questions, answers]).sort_values('ParentId')[['ParentId', 'Id', 'PostTypeId', 'Body']].reset_index(drop=True)
posts['Text'] = posts.apply(convert_html_to_text, axis=1)
posts['Post length'] = posts.apply(text_word_count, axis=1)

posts.hist('Post length', range=(0, 1500))
plt.xlabel('post length')
plt.ylabel('number of posts')
plt.savefig(os.path.join(outputSubdir, 'word_count_hist.png'))
plt.show()

posts.drop('Body', axis=1, inplace=True)
posts.to_csv(os.path.join(outputSubdir, 'posts.csv'), index=False, encoding='utf-8')

