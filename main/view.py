# Импорт биьлиотеки flask
from flask import Blueprint, render_template, request

# Импорт функций
from functions import get_content

import logging
from json import JSONDecodeError


main_blueprint = Blueprint("main_blueprint ", __name__)


@main_blueprint.route('/')
def main_page():
    """ Представление основной страницы"""
    return render_template("index.html")


@main_blueprint.route('/search/')
def search_page():
    """ Представление  страницы поиска"""
    recieved_word = request.args.get('s')
    post = get_content(recieved_word)
    logging.info('Выполнен поиск')
    try:
        if post:
            return render_template("post_list.html", recieved_word=recieved_word, post=post)
        else:
            return "Информация не найдена"
    except JSONDecodeError:
        return 'Файл не удалось преобразовать'
