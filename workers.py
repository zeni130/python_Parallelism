import json
import os
import time

import requests

from adapters import (m_multiprocessing, m_multiprocessing_pool,
                      m_successively, m_threading, m_threading_amount_thr,
                      m_threading_semaphore)


class PageToJsonFile:
    def __init__(self, delay: float):
        self.delay = delay

    def __call__(self, page: int):
        self.page = page
        self.data_url_json(page)

    def data_url_json(self, page: int) -> None:
        response = requests.get(
            url=f"https://jsonplaceholder.typicode.com/posts/{page}"
        ).json()
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


class TestPool:
    def __init__(self, num_pages, page_to_jsonfile, delay, amount_parallel):
        self.num_pages = num_pages
        self.page_to_jsonfile = page_to_jsonfile
        self.delay = delay
        self.amount_parallel = amount_parallel

    def result_successively(self) -> None:
        print(f"=> Working time successively ↓")
        t_start = time.time()
        m_successively.run_suc(
            num_pages=self.num_pages, page_to_jsonfile=self.page_to_jsonfile
        )
        t_end = time.time()
        print(f"==> work_time_suc: {t_end - t_start}")
        time.sleep(self.delay)

    def result_threading_unlimited(self) -> None:
        print(f"=> Working time Threading no flow limit ↓")
        t_start = time.time()
        m_threading.run_thr(
            num_pages=self.num_pages, page_to_jsonfile=self.page_to_jsonfile
        )
        t_end = time.time()
        print(f"==> work_time_thr: {t_end - t_start}")
        time.sleep(self.delay)

    def result_threading(self) -> None:
        print(f"=> Working time Threading, {self.amount_parallel} threads ↓")
        t_start = time.time()
        m_threading_amount_thr.run_thr(
            num_pages=self.num_pages,
            count_thr=self.amount_parallel,
            page_to_jsonfile=self.page_to_jsonfile,
        )
        t_end = time.time()
        print(f"==> work_time_thr: {t_end - t_start}")
        time.sleep(self.delay)

    def result_threading_semaphore(self) -> None:
        print(
            f"=> Working time Threading with semaphore, {self.amount_parallel} threads ↓"
        )
        t_start = time.time()
        m_threading_semaphore.run_thr(
            num_pages=self.num_pages,
            count_thr=self.amount_parallel,
            page_to_jsonfile=self.page_to_jsonfile,
        )
        t_end = time.time()
        print(f"==> work_time_thr_semaphore: {t_end - t_start}")
        time.sleep(self.delay)

    def result_multiprocessing(self) -> None:
        print(f"=> Working time Multiprocessing, {self.amount_parallel} processes ↓")
        t_start = time.time()
        m_multiprocessing.run(
            num_pages=self.num_pages,
            count_proc=self.amount_parallel,
            page_to_jsonfile=self.page_to_jsonfile,
        )
        t_end = time.time()
        print(f"==> work_time_multiproc: {t_end - t_start}")
        time.sleep(self.delay)

    def result_multiprocessing_pool(self) -> None:
        print(
            f"=> Working time Multiprocessing pool, {self.amount_parallel} processes ↓"
        )
        t_start = time.time()
        m_multiprocessing_pool.run(
            num_pages=self.num_pages,
            count_proc=self.amount_parallel,
            page_to_jsonfile=self.page_to_jsonfile,
        )
        t_end = time.time()
        print(f"==> work_time_multiproc_pool: {t_end - t_start}")
        time.sleep(self.delay)
