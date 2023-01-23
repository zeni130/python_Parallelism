import requests
import json
import os
import time


def write_to_json(data: dict, way: str, file_name: str) -> None:
    if not os.path.isdir(f"{way}/data_files"):
        os.mkdir(f"{way}/data_files")

    with open(f"{way}/data_files/{file_name}", "w") as outfile:
        json.dump(data, outfile)


def data_url_json(url: str) -> dict:
    response = requests.get(url)
    return response.json()


def m_successively_def(suc_name) -> None:
    data_json = data_url_json(
        url=f"https://jsonplaceholder.typicode.com/posts/{suc_name}"
    )

    file_name = f"post_{suc_name}"
    way = os.getcwd()
    write_to_json(data=data_json, way=way, file_name=file_name)


def run_suc(amount) -> None:
    t_start = time.time()

    for i in range(1, amount+1):
        m_successively_def(suc_name=f"{i}")

    t_end = time.time()
    print(f"work_time_suc: {t_end - t_start}")


if __name__ == "__main__":
    run_suc(amount=100)
