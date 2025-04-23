from dotenv import load_dotenv
import os
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticDatabase
from pymongo import MongoClient, errors
from pymongo.errors import ConnectionFailure, OperationFailure, NetworkTimeout, ServerSelectionTimeoutError
import logging

load_dotenv()

logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.INFO)

def get_database() -> AgnosticDatabase:
    """
    Returns the database instance.
    """
    if not mongo_uri:
        logger.error("MONGO_URI is not set in the environment variables.")
        raise ValueError("MONGO_URI is not set in the environment variables.")
    try:
        client = MongoClient(MONGO_URI)
        db = client["Personal_Life_Coach"]
        logger.info("MongoDB client initialized successfully.")
        return db
    except (ConnectionFailure, OperationFailure, NetworkTimeout, ServerSelectionTimeoutError) as e:
        logger.error(f"Database connection error: {e}")
        raise e



