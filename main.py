from fastapi import FastAPI
from apps.settings.router import router as settings_router
from apps.reports.router import router as report_router

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'App is running'}

app.include_router(settings_router)
app.include_router(report_router)