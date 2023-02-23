import multiprocessing
import time

from adapters.request_json import PageToJsonFile


def multiprocessing_pool_run(
    num_pages: int, count_proc: int, page_to_json: PageToJsonFile
) -> None:

    with multiprocessing.Pool(count_proc) as p:
        p.map(page_to_json, list(range(1, num_pages + 1)))
        p.close()
        p.join()


if __name__ == "__main__":
    t_start = time.time()
    page_to_jsonfile = PageToJsonFile(delay=0)
    multiprocessing_pool_run(
        num_pages=100, count_proc=10, page_to_json=page_to_jsonfile
    )
    t_end = time.time()
    print(f"==> work_time_multiproc: {t_end - t_start}")
