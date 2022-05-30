import logging
import os

from exceptions import PictureFormatNotSupportedError, PictureNotUploadedError

logger = logging.getLogger("basic")


class UploadManager:

    def is_file_type_valid(self, file_type):
        if file_type.lower() in ['jpg', 'jpeg', 'png', 'gif', 'webp', 'tiff']:
            return True
        return False

    def saving_file(self, picture):
        # Работаем с картинкой
        filename = picture.filename
        file_type = filename.split('.')[-1]

        # Проверяем валидность картинки
        if not self.is_file_type_valid(file_type):
            logger.info("Загруженный файл не картинка")
            raise PictureFormatNotSupportedError(f"Формат {file_type} не поддерживается")

        os_path = os.path.join(".", "uploads", "images", filename)

        # Сохраняем картинку
        try:
            picture.save(os_path)
        except FileNotFoundError:
            logger.error("Ошибка при загрузке файла")
            raise PictureNotUploadedError(f'{os_path}, {filename}')

        return filename
