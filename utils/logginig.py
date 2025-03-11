import logging

class ColorFormatter(logging.Formatter):
    color_format = {
        logging.INFO: "\033[92m[INF] \033[0m",
        logging.WARNING: "\033[93m[WRN] \033[0m",
        logging.ERROR: "\033[91m[ERR] \033[0m",
        logging.CRITICAL: "\033[1;91m[FTL] \033[0m"
    }

    def format(self, record):
        color = self.color_format.get(record.levelno, '')
        record.levelname = color + "\033[0m"

        return super().format(record)

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    formatter = ColorFormatter('%(levelname)s %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger

logger = setup_logging()
