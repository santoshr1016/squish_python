import logging


def func():
    logging.basicConfig(level=logging.DEBUG, filename="out.log")

    logging.debug("Hello, This is DEBUG level logging")
    logging.info("Hello, This is info level logging")
    logging.error("Hello, This is error level logging")
    logging.warning("Hello, This is warning level logging")
    logging.critical("Hello, This is critical level logging")


if __name__ == '__main__':
    func()