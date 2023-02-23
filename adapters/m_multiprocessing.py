import multiprocessing
import time

from adapters.request_json import PageToJsonFile


def m_multiprocessing_def(
    count_page: int, name_proc: int, page_to_json: PageToJsonFile
) -> None:

    for page in range(name_proc * count_page + 1, (name_proc + 1) * count_page + 1):
        page_to_json(page=page)


def multiprocessing_def_run(
    num_pages: int, count_proc: int, page_to_json: PageToJsonFile
) -> None:

    count_page = int(num_pages / num_pages)
    processes = [
        multiprocessing.Process(
            target=m_multiprocessing_def,
            args=(
                int(count_page),
                int(name_proc),
                page_to_json,
            ),
        )
        for name_proc in range(num_pages)
    ]

    for proc in processes:
        proc.start()

    for proc in processes:
        proc.join()


if __name__ == "__main__":
    t_start = time.time()
    page_to_jsonfile = PageToJsonFile(delay=0)
    multiprocessing_def_run(num_pages=100, count_proc=10, page_to_json=page_to_jsonfile)
    t_end = time.time()
    print(f"==> work_time_multiproc: {t_end - t_start}")
