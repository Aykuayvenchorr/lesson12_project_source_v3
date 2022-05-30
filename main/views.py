import logging

from flask import Blueprint, render_template, request, current_app
from classes import DataManager

# Затем создаем новый блюпринт, выбираем для него имя
from exceptions import DataSourceBrokenError

main_blueprint = Blueprint('main_blueprint', __name__)
logger = logging.getLogger("basic")


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    path = current_app.config.get("POST_PATH")
    data_manager = DataManager(path)
    s = request.args.get("s")
    logger.info(f"Выполняется поиск {s}")

    if s:
        posts = data_manager.search_post(s)
        return render_template('post_list.html', s=s, posts=posts)
    return render_template('post_list.html')


@main_blueprint.errorhandler(DataSourceBrokenError)
def data_source_broken_error(e):
    return "Файл с данными поврежден"


