from fastapi import FastAPI
from route import api_routes
from view import swagger_view
from utils.global_variables import GlobalVariables

app = FastAPI()

# Initialize global variables
global_vars = GlobalVariables()

# up api route
app.include_router(api_routes.router)

# Up swagger documentation view
app.include_router(swagger_view.router)

