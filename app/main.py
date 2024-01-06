from fastapi import FastAPI
from .routes.route import router

app = FastAPI()

# Include the router in the application
app.include_router(router)
