from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import re
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import numpy as np

class Preprocessing():

    def __init__(self,df):
        self.df = df

    def rem_nums(self,x):
         # Remove numbers
        x = ''.join(word for word in x if not word.isdigit())
        return x

    def lower_case(self,x):
        return x.lower()

    def rem_special_characters(self,x):
        # Remove special characters
        for punctuation in string.punctuation:
            x = x.replace(punctuation, ' ')
        return x

    def rem_website(self, x):
        # Remove HTTPS, imgs, and user tags
        x = str(x)
        x = re.sub('@[^\s]+','',x)
        x = re.sub('http[^\s]+','',x)
        return x

    def rem_stopwords(self,x):
        # Remove stopwords
        stopw = stopwords.words('english')
        keepwords = ['not',
                'can',
                "don't",
                'couldn',
                "couldn't",
                'should',
                'shouldn',
                "should've",
                "won't",
                'but',
                'mustn',
                "mustn't",
                'wouldn',
                "wouldn't"]
        stopwords2 = [i for i in stopw if i not in keepwords]

        word_tokens = word_tokenize(x)

        x = [w for w in word_tokens if not w in stopwords2]

        return x

    def top2vec_structure(self,x):
        x = " ".join(word for word in x)
        return x

    def lemmatizing(self, x):
        # Lemmatizing
        lemmatizer = WordNetLemmatizer()
        x = [lemmatizer.lemmatize(word) for word in x]
        return x

    def top2vec_preprocessing(self):
        self.df = self.df.applymap(self.rem_website)
        self.df = self.df.applymap(self.rem_special_characters)
        self.df = self.df.applymap(self.rem_stopwords)
        self.df = self.df.applymap(self.top2vec_structure)
        top2vec_input = [i for i in self.df["Tweet"]]
        return top2vec_input

    def sentiment_analysis_preprocessing(self):
        self.df = self.df.applymap(self.rem_website)
        self.df = self.df.applymap(self.rem_special_characters)
        self.df = self.df.applymap(self.lower_case)
        self.df = self.df.applymap(self.rem_nums)
        self.df = self.df.applymap(self.rem_stopwords)
        self.df = self.df.applymap(self.lemmatizing)

if __name__ == '__main__':
    pass
