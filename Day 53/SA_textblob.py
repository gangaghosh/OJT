# textblob library
# create a sample text
# let import textblob over here in the app
from textblob import TextBlob
text=[
     "The quick brown fox jumps over the lazy dog so funny",
     "Python is a popular language ",
     "Natural Language Processing (NLP) is Super",
     "TextBlob is a Python library for NLP"
]

# create function to do the sentiment analysis
def sentiment_analysis(text):
    analysis= TextBlob(text)
#1.0 - 1.0 polarity score
    polarity= analysis.sentiment.polarity
    if polarity>0:
        sentiment="Positive"
    elif polarity<0:
        sentiment="Negative" 
    else:
        sentiment="Neutral"
        return sentiment
for text in text:
    sentiment=sentiment_analysis(text)
    print(f"Text:{text}")
    print(f"Sentiment:{sentiment}")
