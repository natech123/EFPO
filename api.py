from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
from datetime import datetime
import pytz
from EFPO.the_almighty import *
import ipdb

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
@app.get("/")
def index():
    return {"greeting": "Hello world"}
@app.get("/predict")
def predict(search,
            date_beg,
            date_end,
            number):
    date_beg = datetime.strptime(date_beg, "%Y-%m-%d")
    date_end = datetime.strptime(date_end, "%Y-%m-%d")

    query_dict= {'search': [str(search)],
                 'date_beg': [date_beg],
                 'date_end': [date_end],
                 'number': [int(number)]}

    X_pred = pd.DataFrame(query_dict)

    # pipeline = joblib.load('model.joblib')
    model=EFPO_Model(search,date_beg,date_end,number)
    # model = EFPO_Model(query_dict.values)
    df = model.generate_data()
    model.top2vec_fit()
    # model.top_tweet_sentiment
    vis = model.top2vec_visualisation()
    return {'DataFrame':df,
            'Visualisation': vis}
