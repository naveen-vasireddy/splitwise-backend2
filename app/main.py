from fastapi import FastAPI
from app.api.endpoints import group

app = FastAPI()

# Include the group router
app.include_router(group.router, prefix="/api", tags=["Groups"])

@app.get("/")
async def root():
    return {"message": "Welcome to Splitwise-Backend2!"}