import logging
import sys
from datetime import datetime

LOGGING_DATE = datetime.now()
LOGGING_RECORD_FACTORY = logging.getLogRecordFactory()


def _rel_time() -> float:
    time_delta = datetime.now() - LOGGING_DATE
    return time_delta.total_seconds()


def _logger_record_factory(*args, **kwargs):
    record = LOGGING_RECORD_FACTORY(*args, **kwargs)
    record.rel_time = _rel_time()
    return record


logging.setLogRecordFactory(_logger_record_factory)


def init_logging():
    logging_stdout_format = '%(rel_time)+11.6f [ %(levelname) -8s ] %(filename)s:%(lineno) -32s -> %(message)s'
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_formatter = logging.Formatter(logging_stdout_format)
    stdout_handler.setFormatter(stdout_formatter)
    logger.addHandler(stdout_handler)
