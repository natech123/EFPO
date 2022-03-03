
import top2vec
from EFPO.get_data import Get_Data
from EFPO.preprocessing import Preprocessing

class Top2Vec_Model():

    def __init__(self, search, date_beg, date_end, number):
        self.search = search
        self.date_beg = date_beg
        self.date_end = date_end
        self.number = number

    def fit(self):
        data = Get_Data(self.search, self.date_beg, self.date_end, self.number)
        data.tweet_scrape()
        data.simple_preproc()
        df = data.df
        clean_data = Preprocessing(df)
        top2vec_input = clean_data.top2vec_preprocessing()
        self.model = top2vec.Top2Vec(top2vec_input, speed="deep-learn", min_count=5, embedding_model = "universal-sentence-encoder")
