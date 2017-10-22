import pandas
import nltk
import re

from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter

nltk.download('stopwords')

stemmer = PorterStemmer()
tokenizer = RegexpTokenizer('\w+')

stopWords = set(stopwords.words('english'))
posts = pandas.read_csv('posts.csv')['Text']

wordsBeforeStem = []
wordsAfterStem = []
stemTracker = {}
 
for post in posts:
    words = tokenizer.tokenize(post)
    for word in words:
        if word not in stopWords and re.match(r"(?i)\b[a-z_-]+\b", word):
            lowerWord = word.lower()
            wordsBeforeStem.append(lowerWord)
            wordsAfterStem.append(stemmer.stem(lowerWord))
            stemTracker[stemmer.stem(lowerWord)] = lowerWord

# identify the top-20 most frequent words from the dataset (excluding the stop words) before and after performing stemming
# for each of the top-20 most frequent stems, list their original words from which the stem is reached
print(Counter(wordsBeforeStem).most_common(20))
counterAfterStem = Counter(wordsAfterStem).most_common(20)
print(counterAfterStem)
for i in counterAfterStem:
    print(i[0] + ': ' + stemTracker[i[0]])
print("Finished")