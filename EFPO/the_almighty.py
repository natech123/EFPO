from EFPO.get_data import *
from EFPO.preprocessing import *
from EFPO.top2vec import *
from EFPO.sentiment_analysis import *
from top2vec import Top2Vec
import numpy as np

class EFPO_Model():

    def __init__(self,search, date_beg, date_end, number):
        self.search = search
        self.date_beg = date_beg
        self.date_end = date_end
        self.number = number

    def generate_data(self):
        data = Get_Data(self.search, self.date_beg, self.date_end, self.number)
        data.tweet_scrape()
        data.simple_preproc()
        self.df = data.df


    def top2vec_fit(self):
        clean_data = Preprocessing(self.df)
        top2vec_input = clean_data.top2vec_preprocessing()
        self.model = Top2Vec(top2vec_input, speed="deep-learn", min_count=5, embedding_model = "universal-sentence-encoder")

    # def docsearchbytopic(self,topic,num):
    #     rez = self.model.search_documents_by_topic(topic,num_docs=num)
    #     tweetz = [x for x in rez[2]]
    #         tweets = []
    #     for i in tweetz:
    #         tweets.append(indexed_tweets[i])
    #     return tweets

    def top_tweet_sentiment(self,topic):
        model = self.model
        # num_of_topics = model.get_num_topics()
        # for i in np.arange(0,num_of_topics,1):
        top_5 = model.search_documents_by_topic(topic, num_docs=5)
        tweets = top_5[0]
        index = top_5[2]
        tweet = []
        sentiment = []
        for i in index:
                tweet.append(self.df["Tweet"][i])

        temp_df = pd.DataFrame(tweet, columns = "tweets")
        sentiment_df = Preprocessing(temp_df)
        sentiment_df.sentiment_analysis_preprocessing()
        for j in sentiment_df.df["tweets"]:
            sentiment_tweet = Sentiment_Analysis.google(j)
            sentiment.append(sentiment_tweet)

        topic_tweet_sentiment_df = pd.DataFrame([tweet,sentiment], columns=["tweets", "sentiment"])
        return topic_tweet_sentiment_df

    def top2vec_visualisation(self):
        pass
