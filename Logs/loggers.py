import logging


def log_fun():
    logger = logging.getLogger()
    filehandler = logging.FileHandler("LogFile.log")
    formatter = logging.Formatter('')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)

    return logger
