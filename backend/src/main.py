from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.auth.view import auth_router

app = FastAPI()


app.include_router(auth_router)
