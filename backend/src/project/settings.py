import os

from pathlib import Path

from pydantic import BaseSettings
from dotenv import load_dotenv


dotenv_path = Path('.env.local')
load_dotenv(dotenv_path=dotenv_path)

BOT_API_TOKEN = os.environ.get("BOT_TOKEN")
REGISTRY = os.environ.get("REGISTRY")
SERVICE_CHAT_ID = os.environ.get("SERVICE_CHAT_ID")
DOMAIN = os.environ.get("DOMAIN")
BACKEND_PORT = os.environ.get("BACKEND_PORT")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")


class Settings(BaseSettings):
    PROJECT_DIR: Path = "/Users/user/PycharmProjects/clubox-test-task-Artur/backend"
    REGISTRY: str = REGISTRY
    DOMAIN: str = DOMAIN
    BACKEND_PORT: str = BACKEND_PORT
    DEBUG: bool = False

    BOT_TOKEN: str = BOT_API_TOKEN

    SERVICE_CHAT_ID: int = SERVICE_CHAT_ID

    POSTGRES_USER: str = POSTGRES_USER
    POSTGRES_PASSWORD: str = POSTGRES_PASSWORD
    POSTGRES_DB: str = POSTGRES_DB
    POSTGRES_PORT: str = POSTGRES_PORT


settings = Settings()
