from fastapi import FastAPI
from apps.auth.router import router as auth_router
from apps.settings.router import router as settings_router
from apps.settings_dict.router import router as settings_dict_router
from apps.reports.router import router as report_router
from apps.role.router import router as role_router
from apps.role_function.router import router as role_function_router
from apps.functions.router import router as function_router
from apps.departments.router import router as department_router
from apps.modules.router import router as module_router
from apps.modules_company_links.router import router as modules_company_link_router
from apps.status_dict.router import router as status_dict_router
from apps.property_code_dict.router import router as property_code_dict_router
from apps.timezone_dict.router import router as timezone_dict_router
from apps.companies.router import router as company_router
from apps.license.router import router as license_router
from apps.company_properties.router import router as company_property_router
from apps.users.router import router as user_router
from apps.user_groups.router import router as user_groups_router
from apps.user_sendings.router import router as user_sendings_router
from apps.user_properties.router import router as user_properties_router
from apps.user_report_links.router import router as user_report_links_router
from apps.user_roles.router import router as user_roles_router

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'App is running'}

app.include_router(auth_router)
app.include_router(settings_router)
app.include_router(settings_dict_router)
app.include_router(report_router)
app.include_router(role_router)
app.include_router(role_function_router)
app.include_router(function_router)
app.include_router(department_router)
app.include_router(module_router)
app.include_router(modules_company_link_router)
app.include_router(status_dict_router)
app.include_router(property_code_dict_router)
app.include_router(timezone_dict_router)
app.include_router(company_router)
app.include_router(company_router)
app.include_router(license_router)
app.include_router(company_property_router)
app.include_router(user_router)
app.include_router(user_groups_router)
app.include_router(user_sendings_router)
app.include_router(user_properties_router)
app.include_router(user_report_links_router)
app.include_router(user_roles_router)