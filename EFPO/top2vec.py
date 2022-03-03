
from top2vec import Top2Vec
from EFPO.get_data import Get_Data
from EFPO.preprocessing import Preprocessing

class Top2Vec_Model():

    def __init__(self, search, date_beg, date_end, number):
        data = Get_Data(search, date_beg, date_end, number)
        data.tweet_scrape()
        data.simple_preproc()
        df = data.df
        clean_data = Preprocessing(df)
        top2vec_input = clean_data.top2vec_preprocessing()
        self.model = Top2Vec(top2vec_input, speed="deep-learn", min_count=5, embedding_model = "universal-sentence-encoder")
