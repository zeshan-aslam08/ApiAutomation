import logging


def log_fun():
    logger = logging.getLogger()
    filehandler = logging.FileHandler(r"C:\Users\xint\PycharmProjects\ApiTesting\Logs\LogFile.log")
    formatter = logging.Formatter('')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)

    return logger
