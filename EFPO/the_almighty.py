from EFPO.get_data import *
from EFPO.preprocessing import *
from EFPO.top2vec import *
from EFPO.sentiment_analysis import *
from top2vec import Top2Vec
import numpy as np
import umap
import plotly.express as px
from sklearn.preprocessing import StandardScaler

class EFPO_Model():

    def __init__(self,search, date_beg, date_end, number):
        self.search = search
        self.date_beg = date_beg
        self.date_end = date_end
        self.number = number
        self.visdf=None

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
        sentiment = []#
        for i in index:
            tweet.append(self.df.iloc[i])

        temp_df = pd.DataFrame(tweet, columns = ["tweets"])
        sentiment_df = Preprocessing(temp_df)
        sentiment_df.sentiment_analysis_preprocessing()
        for j in sentiment_df.df["tweets"]:
            sentiment_tweet = Sentiment_Analysis.roberta(j)
            sentiment.append(sentiment_tweet)

        topic_tweet_sentiment_df=pd.DataFrame()
        topic_tweet_sentiment_df["tweet"]=tweet
        topic_tweet_sentiment_df["sentiment"]=sentiment
        return topic_tweet_sentiment_df

    def top2vec_visualisation(self):
        model = self.model
        umap_model = umap.UMAP(random_state=42, n_components=3,n_epochs=10000, learning_rate=0.1)
        umap_fit = umap_model.fit(model._get_document_vectors())
        print(umap_fit,type(umap_fit))
        scaled_data = StandardScaler().fit_transform(umap_fit.embedding_)
        og_tweets = []
        topic = []
        vector1 = []
        vector2 = []
        vector3 = []
        size_ = []
        top_tweets_per_topic = []
        top_tweets_sentiment=[]
        for i in np.arange(0,model.get_num_topics(),1):
            list_of_tweets=[]
            sentiment_analysis_topic=[]
            for index,j in enumerate(model.search_documents_by_topic(i, num_docs=model.topic_sizes[i])[2]):
                og_tweets.append(self.df["Tweet"].iloc[j])
                topic.append(str(i))
                vector1.append(float(umap_fit.embedding_[j][0]))
                vector2.append(float(umap_fit.embedding_[j][1]))
                vector3.append(float(umap_fit.embedding_[j][2]))
                size_.append(1)
                if index < 5:
                    list_of_tweets.append(self.df["Tweet"].iloc[j])
                    sentiment_analysis_topic.append(Sentiment_Analysis.roberta(self.df["Tweet"].iloc[j]))

            top_tweets_per_topic.append(list_of_tweets)
            top_tweets_sentiment.append(sentiment_analysis_topic)

        #self.df_umap = pd.DataFrame(data = {"tweets":og_tweets, "topic" : topic,"vector1" : vector1, "vector2" : vector2, "vector3" : vector3})
        print("computation complete")
        self.visdf=[og_tweets,vector1,vector2,vector3,topic,size_,top_tweets_per_topic,top_tweets_sentiment]
        #fig = px.scatter_3d(self.df_umap, x="vector1", y="vector2", z="vector3",
        #      color="topic", hover_data =["tweets"], title='Visualization of tweets in 3D Space', size_max = 10, size = size_)
