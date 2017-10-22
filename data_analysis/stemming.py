import pandas
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter

nltk.download('stopwords')

stemmer = PorterStemmer()
tokenizer = RegexpTokenizer('\w+')

stopWords = set(stopwords.words('english'))
posts = pandas.read_csv('posts.csv', encoding='utf-8')['Text']
wordsBeforeStem = []
wordsAfterStem = {}
 
for post in posts:
    words = tokenizer.tokenize(post)
    for word in words:
        if word not in stopWords:
            lowerWord = word.lower()
            wordsBeforeStem.append(lowerWord)
            wordsAfterStem[stemmer.stem(lowerWord)] = lowerWord
 
# identify the top-20 most frequent words from the dataset (excluding the stop words) before and after performing stemming.
# for each of the top-20 most frequent stems, list their original words from which the stem is reached
try:
    print(Counter(wordsBeforeStem).most_common(20))
    print(Counter(wordsAfterStem).most_common(20))
except UnicodeEncodeError:
    print("Please set console properties to display utf-8. For Windows execute:\n\tchcp 65001\n\tset PYTHONIOENCODING=utf-8\n")
print("Finished")