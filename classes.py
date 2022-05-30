import json

from exceptions import DataSourceBrokenError


class DataManager:

    def __init__(self, path):
        self.path = path

    def json_load(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                file = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            raise DataSourceBrokenError("Файл с данными поврежден")
        return file

    def save_data(self, data):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def search_post(self, query):
        output_data = []
        for post in self.json_load():
            if query in post["content"]:
                output_data.append(post)
        return output_data

    def add_post(self, post):
        posts = self.json_load()
        posts.append(post)
        self.save_data(posts)
