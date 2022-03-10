
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
            tweets.append({"Tweet":tweet.content, "Lang": tweet.lang})
            if i > self.number:
                break
        self.df = pd.DataFrame(tweets)



    def simple_preproc(self):
        """Clean the data by only selecting english language tweets and removing duplicates"""
        #if list(self.df.columns).count("Lang")>0:
        print(self.df.columns,self.df)

        self.df = self.df[self.df["Lang"] == "en"]

        self.df.drop_duplicates(inplace=True)

        self.df.dropna(inplace = True)

        self.df = self.df[["Tweet"]]



if __name__ == '__main__':
    biden_data = Get_Data("biden", "2022-01-01", "2022-03-01", 2)
    biden_data.tweet_scrape()
    biden_data.simple_preproc()
    df = biden_data.df
    print(df.head())
