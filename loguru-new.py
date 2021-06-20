from loguru import logger

logger.debug("Hello, World! (debug)")
logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="100 MB", compression="zip",
           serialize=True)  # serialize=True - в формате JSON
logger.add("debug1.log", format="{time} {level} {message}", level="DEBUG", rotation="100 MB", compression="zip")


def divide(a: int, b: int) -> float:
    logger.info(f"a={str(a)} b={str(b)}")
    return a / b


@logger.catch()
def main():
    return divide(1, 0)


if __name__ == "__main__":
    main()
