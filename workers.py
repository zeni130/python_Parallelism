import requests
import json
import time
import os


class PageToJsonFile:
    def __init__(self, delay: float):
        self.delay = delay

    def __call__(self, page: int):
        self.page = page
        self.data_url_json(page)

    def data_url_json(self, page: int) -> None:
        response = requests.get(url=f"https://jsonplaceholder.typicode.com/posts/{page}").json()
        file_name = f"post_{page}"
        way = os.getcwd()
        self.write_to_json(data=response, way=way, file_name=file_name)

        time.sleep(self.delay)

    @staticmethod
    def write_to_json(data: dict, way: str, file_name: str) -> None:
        if not os.path.isdir(f"{way}/data_files"):
            os.mkdir(f"{way}/data_files")

        with open(f"{way}/data_files/{file_name}", "w") as outfile:
            json.dump(data, outfile)
