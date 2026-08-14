import os
from pathlib import Path
from dotenv import load_dotenv
from typing import Optional


def load_env() -> None:
    load_dotenv()
    print(".env loaded (if present)")


def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)


PROJECT_ROOT = Path.cwd()
DATA_DIR = PROJECT_ROOT / "data"