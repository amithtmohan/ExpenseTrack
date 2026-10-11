from fastapi import FastAPI
from .models import Expense
 


app = FastAPI()


@app.get("/health")
def health():
    return {"Status":"OK"}


#Add POST /expenses that takes that model and returns it back with a made-up id

@app.post("/expenses")
def add_expenses(exp:Expense):
    return {"id": 1, **exp.model_dump()}