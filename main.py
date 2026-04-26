from fastapi import FastAPI
from router import router as player_router
from databaseconnect import base, engine, SessionLocal


app = FastAPI()

app.include_router(player_router)


base.metadata.create_all(bind=engine)




