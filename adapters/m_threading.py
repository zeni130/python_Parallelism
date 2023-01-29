import threading
import time

from workers import PageToJsonFile


def run_thr(num_pages: int, page_to_jsonfile: PageToJsonFile) -> None:

    thrs = [
        threading.Thread(
            target=page_to_jsonfile,
            args=(str(page),),
            name=f"thr-{page}",
        )
        for page in range(1, num_pages + 1)
    ]

    for page in thrs:
        page.start()

    for page in thrs:
        page.join()


if __name__ == "__main__":
    t_start = time.time()
    page_to_jsonfile = PageToJsonFile(delay=0)
    run_thr(num_pages=100, page_to_jsonfile=page_to_jsonfile)
    t_end = time.time()
    print(f"==> work_time_thr: {t_end - t_start}")
