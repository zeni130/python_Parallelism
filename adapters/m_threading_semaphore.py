import time
from threading import BoundedSemaphore, Thread

from workers import PageToJsonFile


def run_thr(num_pages: int, count_thr: int, page_to_jsonfile: PageToJsonFile) -> None:

    pool = BoundedSemaphore(value=count_thr)

    def sem_pool(page: int) -> None:
        with pool:
            page_to_jsonfile(page)

    thrs = [
        Thread(
            target=sem_pool,
            args=(str(thread),),
            name=f"thr-{thread}",
        )
        for thread in range(1, num_pages + 1)
    ]

    for thr in thrs:
        thr.start()

    for thr in thrs:
        thr.join()


if __name__ == "__main__":
    t_start = time.time()
    page_to_jsonfile = PageToJsonFile(delay=0)
    run_thr(num_pages=100, count_thr=10, page_to_jsonfile=page_to_jsonfile)
    t_end = time.time()
    print(f"==> work_time_thr: {t_end - t_start}")
