from fastapi import FastAPI
from pydantic import BaseModel
from paystack import Payment
import secret

reference_value = None

class User(BaseModel):
    email : str
    cash : int

app = FastAPI()

@app.post("/User/")
def get_user_info(user_input: User): 
     email = user_input.email
     cash = user_input.cash
     apple = Payment(secret.secret, email, cash)
     return apple.status()

