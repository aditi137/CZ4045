#identify the top-20 most frequent words from the dataset (excluding the stop words) before and after performing stemming.
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
posts = pandas.read_csv('posts.csv', encoding='utf-8')['Text'][1:4]

wordsBeforeStem = []
wordsAfterStem = []

for post in posts:
    words = tokenizer.tokenize(post)
    for word in words:
        if word not in stopWords:
            lowerWord = word.lower()
            wordsBeforeStem.append(lowerWord)
            wordsAfterStem.append(stemmer.stem(lowerWord))

print(Counter(wordsBeforeStem))
print(Counter(wordsAfterStem))
print("Finished")