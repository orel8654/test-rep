from fastapi import FastAPI
from apps.users.router import router as user_router
from apps.settings.router import router as settings_router

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'App is running'}

app.include_router(user_router)
app.include_router(settings_router)