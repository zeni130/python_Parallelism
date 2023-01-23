import requests
import json
import os
import threading
import time


def write_to_json(data: dict, way: str, file_name: str) -> None:
    if not os.path.isdir(f"{way}/data_files"):
        os.mkdir(f"{way}/data_files")

    with open(f"{way}/data_files/{file_name}", "w") as outfile:
        json.dump(data, outfile)


def data_url_json(url: str) -> dict:
    response = requests.get(url)
    return response.json()


def m_treading_def(thr_name) -> None:

    data_json = data_url_json(
        url=f"https://jsonplaceholder.typicode.com/posts/{thr_name}"
    )

    file_name = f"post_{thr_name}"
    way = os.getcwd()
    write_to_json(data=data_json, way=way, file_name=file_name)


def run_thr(amount) -> None:
    thr_list = []
    t_start = time.time()

    for i in range(1, amount+1):
        thr = threading.Thread(
            target=m_treading_def,
            args=(
                str(i),
            ),
            name=f"thr-{i}",
        )
        thr_list.append(thr)
        thr.start()

    for i in thr_list:
        i.join()

    t_end = time.time()
    print(f"work_time_thr: {t_end - t_start}")


if __name__ == "__main__":
    run_thr(amount=100)
