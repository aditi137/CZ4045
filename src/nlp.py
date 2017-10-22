# Just a sample program that does the following:
# 1. downloads and extracts text content of web page
# 2. splits the text into sentences and counts sentences
# 3. splits the text into tokens and counts token types
# 4. finds lemmas (or stems) of the tokens and counts lemma types
# 5. does stemming on the tokens and counts unique stemmed tokens

from urllib.request import urlopen
from bs4 import BeautifulSoup
import nltk

def get_text(url):
	html = urlopen(url).read()
	soup = BeautifulSoup(html, "html.parser")
	text = soup.get_text()
	return text
	
def get_sentences(text):
#	nltk.download('punkt')
	sentences = nltk.tokenize.sent_tokenize(text)
	return sentences
	
def get_tokens(text):	
	tokens = nltk.tokenize.word_tokenize(text)
	token_types = set(tokens)
	return tokens, token_types
	
def get_lemmas(token_types):
	wnl= nltk.stem.WordNetLemmatizer()
#	nltk.download('wordnet')
	lemma_types = set(wnl.lemmatize(token_type) for token_type in token_types)
	return lemma_types
	
def get_stems(token_types):
	stemmer = nltk.stem.porter.PorterStemmer()
	stemmed_types = set(stemmer.stem(token_type) for token_type in token_types)
	return stemmed_types


url = "https://stackoverflow.com/questions/46515267/pandas-get-day-of-week-from-date-type-column"
text = get_text(url)
sentences = get_sentences(text)
tokens, token_types = get_tokens(text)
lemma_types = get_lemmas(token_types)
stemmed_types = get_stems(token_types)
print("Number of sentences:", len(sentences))
print("Number of tokens:", len(tokens))
print("Number of token types:", len(token_types))
print("Number of lemma types:", len(lemma_types))
print("Number of stemmed types:", len(stemmed_types))