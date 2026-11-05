import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.core.config import settings


def test_app_name():
    assert settings.app_name == "SupplyPrescript API"


def test_app_version():
    assert settings.app_version == "1.0.0"


def test_database_url_is_configured():
    assert settings.database_url.startswith("postgresql+psycopg://")
