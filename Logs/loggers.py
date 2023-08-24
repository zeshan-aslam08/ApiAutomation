import logging


def log_fun():
    logger = logging.getLogger()
    filehandler = logging.FileHandler(r"C:\Users\xint\PycharmProjects\ApiTesting\Logs\LogFile.log")
    formatter = logging.Formatter('')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)

    return logger
# %(acstime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s
# , datefmt='%d%m%Y %I:%M:%S %p'
