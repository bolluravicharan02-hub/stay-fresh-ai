import sys
from pathlib import Path

from loguru import logger

from app.config import settings


LOG_PATH = Path(settings.LOG_DIR)
LOG_PATH.mkdir(exist_ok=True)

logger.remove()

# Console Logger
logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
           "<level>{message}</level>",
)

# File Logger
logger.add(
    LOG_PATH / "stayfresh.log",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    level="INFO",
    enqueue=True,
    backtrace=True,
    diagnose=True,
)

app_logger = logger