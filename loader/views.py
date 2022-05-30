import os

from flask import Blueprint, render_template, request, current_app
from classes import DataManager
from loader.upload_manager import UploadManager

from exceptions import PictureFormatNotSupportedError, PictureNotUploadedError

# создаем новый блюпринт, выбираем для него имя
loader_blueprint = Blueprint('loader_blueprint', __name__)


@loader_blueprint.route('/post/', methods=["GET"])
def page_form():
    return render_template('post_form.html')


@loader_blueprint.route('/post/', methods=["POST"])
def page_create_posts():

    path = current_app.config.get("POST_PATH")
    data_manager = DataManager(path)
    upload_manager = UploadManager()

    # Получаем данные
    picture = request.files.get("picture")
    content = request.values.get("content")

    # Сохраняем картинку с помощью менеджера загрузки
    filename = upload_manager.saving_file(picture)

    # Формируем путь для браузера клиента
    web_path = os.path.join("/", "uploads", "images", filename)
    pic = web_path

    # Создаем данные для записи в файл
    post = {"pic": web_path, "content": content}

    # Добавляем данные в файл
    data_manager.add_post(post)

    return render_template('post_uploaded.html', pic=pic, content=content)


@loader_blueprint.errorhandler(PictureFormatNotSupportedError)
def error_format(e):
    return f"{e}"


@loader_blueprint.errorhandler(PictureNotUploadedError)
def error_format(e):
    return f"Не удалось загрузить картинку {e}"

