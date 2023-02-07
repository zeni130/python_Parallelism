import multiprocessing
import time

from workers import PageToJsonFile


def run(num_pages: int, count_proc: int, page_to_jsonfile: PageToJsonFile) -> None:

    with multiprocessing.Pool(count_proc) as p:
        p.map(page_to_jsonfile, list(range(1, num_pages + 1)))
        p.close()
        p.join()


if __name__ == "__main__":
    t_start = time.time()
    page_to_jsonfile = PageToJsonFile(delay=0)
    run(num_pages=100, count_proc=10, page_to_jsonfile=page_to_jsonfile)
    t_end = time.time()
    print(f"==> work_time_multiproc: {t_end - t_start}")
