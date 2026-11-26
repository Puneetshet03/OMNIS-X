"""OMNIS-X Backend Configuration and Runtime Settings."""

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
BACKEND_DIR = Path(__file__).resolve().parent.parent
ROOT_DATA_CSV = BASE_DIR / "data" / "omnis_x_200_students(1).csv"
BUNDLED_DATA_CSV = BACKEND_DIR / "app" / "data" / "omnis_x_200_students(1).csv"
CSV_PATH = ROOT_DATA_CSV if ROOT_DATA_CSV.exists() else BUNDLED_DATA_CSV
DATA_DIR = CSV_PATH.parent

load_dotenv(BACKEND_DIR / ".env")
load_dotenv(BASE_DIR / ".env")


class Settings:
    """Validated runtime settings for OMNIS-X."""

    def __init__(self) -> None:
        self.app_env: str = os.getenv("APP_ENV", "development").strip()
        self.frontend_url: str = os.getenv("FRONTEND_URL", "http://localhost:5173").strip()
        self.csv_path: Path = CSV_PATH


settings = Settings()
