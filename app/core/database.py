import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB connection string
MONGO_CONNECTION_STRING = os.getenv("MONGO_CONNECTION_STRING")

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)

# Database reference
db = client["splitwise"]