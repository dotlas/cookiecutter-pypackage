from sys import stdout

from loguru import logger


log_handler_id: int | None = None


def set_logger_level(level: str | int):
    """Sets the minimum level for the logger to send a message to the sink.

    Args:
        level (Union[str, int]): log level
    """
    global log_handler_id

    # Remove existing logger handler
    logger.remove(log_handler_id)

    # Change logger level
    log_handler_id = logger.add(sink=stdout, level=level)


def main():
    # Remove default logger output destination
    logger.remove()

    # Create default logger handler
    log_handler_id = logger.add(sink=stdout)


if __name__ == "__main__":
    main()
