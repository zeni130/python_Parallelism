import threading
import time

from workers import PageToJsonFile


def m_treading_def(count_page: int, name_thr: int, page_to_jsonfile: PageToJsonFile) -> None:

    for page in range(name_thr * count_page + 1, (name_thr + 1) * count_page + 1):
        page_to_jsonfile(page=page)


def run_thr(num_pages: int, count_thr: int, page_to_jsonfile: PageToJsonFile) -> None:
    t_start = time.time()

    count_page = int(num_pages / count_thr)
    thrs = [
        threading.Thread(
            target=m_treading_def,
            args=(
                int(count_page),
                int(name_thr),
                page_to_jsonfile,
            ),
            name=f"thr-{name_thr}"
        ) for name_thr in range(count_thr)
    ]

    for thr in thrs:
        thr.start()

    for thr in thrs:
        thr.join()

    t_end = time.time()
    print(f"==> work_time_thr: {t_end - t_start}")


if __name__ == "__main__":
    page_to_jsonfile = PageToJsonFile(delay=0)
    run_thr(num_pages=100, count_thr=10, page_to_jsonfile=page_to_jsonfile)
