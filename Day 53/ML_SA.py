# Data Collection, Preprocessing
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# create a sample dataset

data=[
     ("I live NLP","Positive"),
     ("I hate this TECHNOLOGY","Negative"),
     ("Its okay, nothing special","Neutral")
]
# seperate all the sentence and labels


sentence,labels=zip(*data)
# downloaded the kits form the library which we have been imported
nltk.download ('punkt')
nltk.download('stopwords')
# intialized the stopwords with assigning the language
stop_words=set(stopwords.words('english'))

def preprocess(text):
     tokens=word_tokenize(text.lower())

     # remove the stop word and punctuation
     filtered_tokens=[word for word in tokens if word.isalnum() and word not in stop_words]
     return " ".join(filtered_tokens)

# preprocess for the sentence which we pass as data
preprocessed_sentences=[preprocess(sentence)for sentence in sentence]

# feature extraction
vectorizer=TfidfVectorizer()
x=vectorizer.fit_transform(preprocessed_sentences)

# split the data into training as well  as test data for model training and evaluation
x_train,x_test,y_train,y_test=train_test_split(x,labels,test_size=0.2,random_state=42)

# train naive bayes classifier 
classifier=MultinomialNB()
classifier.fit(x_train,y_train)

# we can write the code of prediction y from x
y_pred=classifier.predict(x_test)

# evaluating model
accuracy=accuracy_score(y_test,y_pred)
report=classification_report(y_test,y_pred)

print(f"Accuracy:{accuracy}")
print(f"Classification Report:\n{report}")



