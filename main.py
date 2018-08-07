import pandas as pd
import os
from bs4 import BeautifulSoup
import re
import nltk

train = pd.read_csv(os.path.normpath("C:/Users/eliranko/Downloads/labeledTrainData.tsv")
                    , header=0, delimiter="\t", quoting=3)
example1 = BeautifulSoup(train["review"][0])
letters_only = re.sub("[^a-zA-Z]",           # The pattern to search for
                      " ",                   # The pattern to replace it with
                      example1.get_text() )  # The text to search
lower_case = letters_only.lower()        # Convert to lower case
words = lower_case.split()               # Split into words
nltk.download()