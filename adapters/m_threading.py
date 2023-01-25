import threading
import time

from workers import PageToJsonFile


def run_thr(num_pages: int, page_to_jsonfile: PageToJsonFile) -> None:
    t_start = time.time()

    thr_list = []
    for page in range(1, num_pages + 1):
        thr = threading.Thread(
            target=page_to_jsonfile,
            args=(
                str(page),
            ),
            name=f"thr-{page}",
        )
        thr_list.append(thr)
        thr.start()

    for page in thr_list:
        page.join()

    t_end = time.time()
    print(f"==> work_time_thr: {t_end - t_start}")


if __name__ == "__main__":
    page_to_jsonfile = PageToJsonFile(delay=0)
    run_thr(num_pages=100, page_to_jsonfile=page_to_jsonfile)
