#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import urllib.request
from google.cloud import language_v1


# In[2]:


#!pip install transformers
#!pip3 install torch==1.10.2+cu102 torchvision==0.11.3+cu102 torchaudio===0.10.2+cu102 -f https://download.pytorch.org/whl/cu102/torch_stable.html
#!pip install google-cloud-language
#!pip install snscrape
#!pip install nltk


# In[3]:


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import re
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import numpy as np


# In[4]:


from EFPO.get_data import Get_Data
from EFPO.preprocessing import *


# In[5]:


df=Get_Data("euphoria","2020-01-01","2022-01-01",10)


# In[6]:


df.tweet_scrape()


# In[7]:


df.df


# In[8]:


clean_df=Preprocessing(df.df)


# In[9]:


clean_df.top2vec_preprocessing()


# In[10]:


class Sentiment_Analysis():
    def __init__(self,df):
        self.df=df
    def sentiment_analysis_statement(self,text):
        task='sentiment'
        MODEL = f"cardiffnlp/twitter-roberta-base-{task}"
        tokenizer = AutoTokenizer.from_pretrained(MODEL)
        model = AutoModelForSequenceClassification.from_pretrained(MODEL)
        model.save_pretrained(MODEL)
        tokenizer.save_pretrained(MODEL)
        encoded_input = tokenizer(text, return_tensors='pt')
        output = model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        if scores.argmax()==2:
            return "positive"
        elif scores.argmax()==1:
            return "negative"
        else:
            return "neutral"
    def google_analyze_sentiment2(self,text_content):
        """
        Analyzing Sentiment in a String
        Args:
          text_content The text content to analyze
        """
        client = language_v1.LanguageServiceClient()
        type_ = language_v1.Document.Type.PLAIN_TEXT
        language = "en"
        document = {"content": text_content, "type_": type_}#, "language": language}
        encoding_type = language_v1.EncodingType.UTF8
        response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
        if response.document_sentiment.score > 0.33:
            return "positive"
        elif response.document_sentiment.score < -0.33:
            return "negative"
        else:
            return "neutral"

        
    def list_to_string(self,lst):
        return " ".join(lst)
    
    def get_score(self):
        self.df["Tweet_string"]=np.vectorize(self.list_to_string)(self.df["Tweet"])
        self.df["google_sentiment"]=np.vectorize(self.google_analyze_sentiment2)(self.df["Tweet_string"])
        self.df["roberta_sentiment"]=np.vectorize(self.sentiment_analysis_statement)(self.df["Tweet_string"])


# In[11]:


sentiment_df=Sentiment_Analysis(clean_df.df)


# In[12]:


get_ipython().run_cell_magic('time', '', 'sentiment_df.get_score()')


# In[13]:


sentiment_df.df

