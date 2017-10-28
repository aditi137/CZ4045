import os
import re
import pandas
import matplotlib.pyplot as plt


def detect_negation(row):
    try:
        text = row['Text']
        negation_words = re.findall(r'(not|never|none|nobody|no)', text, re.IGNORECASE)
        return len(negation_words)
    except:
        return 0


inputSubDir = 'InputData'
outputSubDir = 'OutputData'
posts = pandas.read_csv(os.path.join(inputSubDir, 'posts.csv'))
posts['NumNegWords'] = posts.apply(detect_negation, axis=1)
num_posts_with_neg = posts.loc[posts['NumNegWords'] > 0, :].shape[0]
per = num_posts_with_neg * 100.0 / posts.shape[0]

plt.hist(posts['NumNegWords'], bins=range(0, 20, 1), histtype='bar', ec='black')
plt.xlabel('Number of negative words')
plt.ylabel('Number of posts')
plt.title('Negation Expressions count')
plt.savefig(os.path.join(outputSubDir, 'negation_expression_count.png'))
plt.text(8, 500, "%d posts (%.2f%%) \nhave negation expressions" % (num_posts_with_neg, per),
         bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
plt.show()
