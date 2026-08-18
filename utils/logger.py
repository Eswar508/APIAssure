import logging
def logger():
    logger = logging.getLogger("apilogs")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler("api_test.log")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger