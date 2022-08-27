# Импорт библиотеки json
import json


def get_text():
    """ Преобразование json файла в python файл"""

    with open("posts.json", "r", encoding='UTF-8') as file:
        file_read = file.read()
        pyt_file = json.loads(file_read)
    return pyt_file


def get_content(text):
    """ Поиск введенного слова"""

    elements_list = []
    for element in get_text():
        if text.lower() in element["content"].lower():
            elements_list.append(element)
    return elements_list


def load_json_file(path, added_page):
    """ Добавление нового тееста и фото в json файл"""

    word_diction = {}
    word_diction["pic"] = '/' + path
    word_diction["content"] = f"{added_page}"
    with open("posts.json", "r", encoding="UTF-8") as file:
        data = json.load(file)
        data.append(word_diction)
    with open("posts.json", "w", encoding="UTF-8") as file:
        new_file = json.dump(data, file, ensure_ascii=False)
    return new_file


def is_filename_allowed(filename):
    """Определение расширения загружаемого файла"""

    allowed_extensions = ['png', 'jpg', 'jpeg']
    extension = filename.split(".")[-1].lower()
    if extension in allowed_extensions:
        return True
    else:
        return False
