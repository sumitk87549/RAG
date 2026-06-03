from fastapi import FastAPI
from api.upload import router as urouter

app = FastAPI()

app.include_router(urouter)

@app.get("/")
def alive():
    return {'KnockKnock???':'I am Alive!!!'}