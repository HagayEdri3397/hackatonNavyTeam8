import pandas as pd
import os
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords # Import the stop word list
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.ensemble import RandomForestClassifier

def review_to_words( raw_review ):
    # 1. Remove HTML
    review_text = BeautifulSoup(raw_review).get_text() 
    # 2. Remove non-letters    
    letters_only = re.sub("[^a-zA-Z]", " ", review_text) 
    # 3. Convert to lower case, split into individual words
    words = letters_only.lower().split()                             
    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))                  
    # 5. Remove stop words
    meaningful_words = [w for w in words if not w in stops]   
    # 6. Join the words back into one string separated by space, 
    # and return the result.
    return( " ".join( meaningful_words ))   

train = pd.read_csv(os.path.normpath("data/labeledTrainData.tsv")
                    , header=0, delimiter="\t", quoting=3)

# Initialize the "CountVectorizer" object, which is scikit-learn's
# bag of words tool.  
vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 5000) 

# Initialize an empty list to hold the clean reviews
clean_train_reviews = []

# Loop over each review; create an index i that goes from 0 to the length
# of the movie review list 
for i in range( train["review"].size ):
    # Call our function for each one, and add the result to the list of
    # clean reviews
    clean_train_reviews.append( review_to_words( train["review"][i] ) )
    if( (i+1)%1000 == 0 ):
        print ("Review %d of %d\n" % ( i+1, train["review"].size ))

# fit_transform() does two functions: First, it fits the model
# and learns the vocabulary; second, it transforms our training data
# into feature vectors. The input to fit_transform should be a list of 
# strings.
train_data_features = vectorizer.fit_transform(clean_train_reviews)

# Numpy arrays are easy to work with, so convert the result to an 
# array
train_data_features = train_data_features.toarray()

# Take a look at the words in the vocabulary
vocab = vectorizer.get_feature_names()

# Sum up the counts of each vocabulary word
dist = np.sum(train_data_features, axis=0)

# Initialize a Random Forest classifier with 100 trees
forest = RandomForestClassifier(n_estimators = 100)

# Fit the forest to the training set, using the bag of words as 
# features and the sentiment labels as the response variable
#
# This may take a few minutes to run
forest = forest.fit( train_data_features, train["sentiment"] )

def examineText(str):
    return forest.predict(vectorizer.transform([str]).toarray())[0]

from tkinter import *
from PIL import ImageTk,Image
window = Tk()
window.title("Bag of Words Meets Bags of Popcorn")
window.geometry('1100x600')
#Tittel
lbl = Label(window, text="Bag of Words Meets Bags of Popcorn",font=("Arial Bold", 40))
lbl.grid(row=0)
#space
sp = Label(window, text="     ",font=("Arial Bold", 20))
sp.grid(row=3)
lbl2 = Label(window, text="Enter text to analyze:",font=("Arial Bold", 20))
lbl2.grid(row=4)
#space

spp = Label(window, text="     ",font=("Arial Bold", 20))
spp.grid(row=5)

#to get the text txt.get()
txt = Entry(window,width=50)
txt.grid(row=7)

def clicked():
    lbClick.configure(text=str(examineText(txt.get())))

def clickedR():
	lbClick.configure(text=""                    "")

#btn = Button(window, text="Click Me", command=clicked)
#column=0, 
btn = Button(window, text="Analyze", command=clicked)
btn.grid(row=8)
btnR = Button(window, text="Reset", command=clickedR)
btnR.grid(row=9)

lbClick = Label(window, text="                    ",font=("Arial Bold", 40))
lbClick.grid( row=10)

window.mainloop()