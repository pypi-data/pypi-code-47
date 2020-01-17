import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path


def configure_logger(log_level: str = "INFO", log_path: Path = None) -> None:
    """Configure the logging to stdout and optionally local file and GCP stackdriver."""
    log_handlers = [logging.StreamHandler(sys.stdout)]

    if log_path is not None:
        log_path.mkdir(parents=True, exist_ok=True)
        log_file = log_path.joinpath("cdf-ifs-file-extractor.log")
        log_handlers.append(TimedRotatingFileHandler(log_file, when="midnight", backupCount=7))

    logging.basicConfig(
        level=logging.INFO if log_level.upper() == "INFO" else log_level,
        format="%(asctime)s %(name)s %(levelname)s - %(message)s",
        handlers=log_handlers,
    )

    _configure_stackdriver_logging()


def _configure_stackdriver_logging() -> None:
    """Send logs to GCP stackdriver. Must be configured with GOOGLE_APPLICATION_CREDENTIALS."""
    if os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        try:
            import google.cloud.logging
        except ImportError:
            logging.warning("GOOGLE_APPLICATION_CREDENTIALS set but google-cloud-logging not available")
        else:
            google.cloud.logging.Client().setup_logging(name="cdf-ifs-file-extractor")
