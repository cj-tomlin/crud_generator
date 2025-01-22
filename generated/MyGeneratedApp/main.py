from fastapi import FastAPI
from routes import user_routes

app = FastAPI(title="Generated FastAPI Application")


app.include_router(user_routes.router, prefix="/users", tags=["User"])
