import logging
import os

project_path = os.getcwd()

file_path = "\\logs\\basic.txt"

full_path = project_path + file_path



def create_logger():
    logger = logging.getLogger("basic")
    logger.setLevel("DEBUG")

    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(full_path)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Добавляем форматтеры
    formatter_one = logging.Formatter("%(asctime)s : %(message)s")

    console_handler.setFormatter(formatter_one)
    file_handler.setFormatter(formatter_one)
