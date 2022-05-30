class DataSourceBrokenError(Exception):
    """Класс для ошибки, когда файл поврежден"""
    pass


class PictureFormatNotSupportedError(Exception):
    """Класс для ошибки, когда файл загружен в недопустимом формате"""
    pass


class PictureNotUploadedError(Exception):
    """Класс для ошибки, когда файл не загружен"""
    pass