"""
This script sets up different logging handlers for the Core module.
It provides console, file, and mail logging capabilities based on the
 provided settings.
"""
import logging
from datetime import datetime
from pathlib import Path

from processing.utils import PROJECT_NAME


def _setup_console_handler(logger: logging.Logger, log_level: int) -> None:
    """
    Configure a console handler for the given logger
    :param logger: The logger instance to set up a console handler for
    :type logger: logging.Logger
    :param log_level: The log level for the console handler
    :type log_level: int
    :return: None
    :rtype: NoneType
    """
    handler: logging.StreamHandler = logging.StreamHandler()  # type: ignore
    handler.setLevel(log_level)
    logger.addHandler(handler)


def _create_logs_folder() -> Path:
    """
    Create a logs folder if it doesn't already exist
    :return: The path to the logs folder
    :rtype: Path
    """
    project_root: Path = Path(__file__).resolve().parent
    while project_root.name != PROJECT_NAME:
        project_root = project_root.parent
    logs_folder_path: Path = project_root / "logs"
    logs_folder_path.mkdir(parents=True, exist_ok=True)
    return logs_folder_path


def _build_log_filename() -> str:
    """
    Create a log filename using the current date and configured date
     format.
    :return: The filename for the log file
    :rtype: str
    """
    return f"log-{datetime.today().strftime('%d-%b-%Y-%H-%M-%S')}.log"


def _configure_file_handler(
    log_filename: str, log_level: int
) -> logging.FileHandler:
    """
    Configure a file handler with the given filename and log level
    :param log_filename: The filename for the log file
    :type log_filename: str
    :param log_level: The log level for the file handler
    :type log_level: int
    :return: A configured file handler
    :rtype: logging.FileHandle
    """
    fmt: str = (
        "[%(name)s][%(asctime)s][%(levelname)s][%(module)s]"
        "[%(funcName)s][%(lineno)d]: %(message)s"
    )
    date_fmt: str = "%Y-%m-%d %H:%M:%S"
    formatter: logging.Formatter = logging.Formatter(fmt, date_fmt)
    file_handler: logging.FileHandler = logging.FileHandler(log_filename)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    return file_handler


def _setup_file_handler(
    logger: logging.Logger,
    log_level: int,
) -> None:
    """
    Configure a file handler for the given logger
    :param logger: The logger instance to set up a file handler for
    :type logger: logging.Logger
    :param log_level: The log level for the file handler
    :type log_level: int
    :return: None
    :rtype: NoneType
    """
    logs_folder_path: Path = _create_logs_folder()
    log_filename: str = _build_log_filename()
    filename_path: str = f"{logs_folder_path}/{log_filename}"
    file_handler = _configure_file_handler(filename_path, log_level)
    logger.addHandler(file_handler)
    file_handler.flush()


def setup_logging(
    log_level: int = logging.ERROR,
) -> None:
    """
    Initialize logging for the application
    :param log_level: The log level to use for the application.
     Defaults to DEBUG
    :type log_level: int
    :return: None
    :rtype: NoneType
    """
    logger: logging.Logger = logging.getLogger()
    logger.handlers.clear()
    logger.propagate = False
    logger.setLevel(log_level)
    _setup_console_handler(logger, log_level)
    _setup_file_handler(logger, log_level)
