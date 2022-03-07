from fastapi import FastAPI
from EFPO import the_almighty


app = FastAPI()

# define a root `/` endpoint
@app.get("/")
def index():
    return {"ok": True}
