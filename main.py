from fastapi import FastAPI
from schemas import Data
from config import REDIS_HOST, REDIS_PORT
import redis

app = FastAPI()
redis_db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)


@app.post("/write_data")
def write_data(data: Data):
    redis_db.set(data.phone, data.address)
    return {"message": "Data written successfully"}


@app.get("/check_data")
def check_data(phone: str):
    address = redis_db.get(phone)
    if address:
        return {"address": address}
    else:
        return {"message": "Address not found"}
