from fastapi import FastAPI
from apps.settings.router import router as settings_router
from apps.settings_dict.router import router as settings_dict_router
from apps.reports.router import router as report_router
from apps.role.router import router as role_router
from apps.functions.router import router as function_router

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'App is running'}

app.include_router(settings_router)
app.include_router(settings_dict_router)
app.include_router(report_router)
app.include_router(role_router)
app.include_router(function_router)