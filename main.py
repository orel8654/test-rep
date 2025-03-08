from fastapi import FastAPI
from apps.settings.router import router as settings_router
from apps.settings_dict.router import router as settings_dict_router
from apps.reports.router import router as report_router
from apps.role.router import router as role_router
from apps.role_function.router import router as role_function_router
from apps.functions.router import router as function_router
from apps.departments.router import router as department_router
from apps.modules.router import router as module_router
from apps.status_dict.router import router as status_dict_router
from apps.property_code_dict.router import router as property_code_dict_router

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'App is running'}

app.include_router(settings_router)
app.include_router(settings_dict_router)
app.include_router(report_router)
app.include_router(role_router)
app.include_router(role_function_router)
app.include_router(function_router)
app.include_router(department_router)
app.include_router(module_router)
app.include_router(status_dict_router)
app.include_router(property_code_dict_router)