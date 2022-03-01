
import pandas as pd
import snscrape.modules.twitter as sntwitter

class Get_Data():

    def __init__(self,search, date_beg, date_end, number):
        self.search = search
        self.date_beg = date_beg
        self.date_end = date_end
        self.number = number

    def tweet_scrape(self):
        """Loads tweets using snscraper, search is the query topic to search, followed by the date parameters,
        followed by the number of tweets we want to gather"""
        tweets = []

        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{self.search} since:{self.date_beg} until:{self.date_end}').get_items()):
            if i > self.number:
                break

            tweets.append({"Tweet":tweet.content, "Lang": tweet.lang})


        self.df = pd.DataFrame(tweets)



    def simple_preproc(self):
        """Clean the data by only selecting english language tweets and removing duplicates"""
        self.df = self.df[self.df["Lang"] == "en"]

        self.df.drop_duplicates(inplace=True)

        self.df.dropna(inplace = True)

        self.df = self.df[["Tweet"]]




if __name__ == '__main__':
    pass
