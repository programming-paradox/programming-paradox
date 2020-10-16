import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

# Getting the article and parsing and summarizing it
url = 'https://images.dawn.com/news/1185903/sanjay-dutt-opens-up-about-his-battle-with-cancer'
article = Article(url)
article.download()
article.parse()

article.nlp()  # For the sentiment Analysis

# Printing the data
print("---------Title--------")
print(f'The title of the article is {article.title}')
print("---------Author----------")
print(f' \n Author of the article is {article.authors}')
print("---------Publication Date----------")
print(f' \n Publication date of the article is {article.publish_date}')
print("---------Summary Date----------")
print(f' \n The Summary Is {article.summary}')


# Doing The Sentiment Analysis
analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative"}')
