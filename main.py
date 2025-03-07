from fastapi import FastAPI
from apps.users.router import router as user_router

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'App is running'}

app.include_router(user_router)