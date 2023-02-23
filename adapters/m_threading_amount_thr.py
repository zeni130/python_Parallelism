import threading
import time

from adapters.request_json import PageToJsonFile


def m_treading_def(
    count_page: int, name_thr: int, page_to_jsonfile: PageToJsonFile
) -> None:

    for page in range(name_thr * count_page + 1, (name_thr + 1) * count_page + 1):
        page_to_jsonfile(page=page)


def run_thr_def(num_pages: int, count_thr: int, page_to_json: PageToJsonFile) -> None:

    count_page = int(num_pages / count_thr)
    thrs = [
        threading.Thread(
            target=m_treading_def,
            args=(
                int(count_page),
                int(name_thr),
                page_to_json,
            ),
            name=f"thr-{name_thr}",
        )
        for name_thr in range(count_thr)
    ]

    for thr in thrs:
        thr.start()

    for thr in thrs:
        thr.join()


if __name__ == "__main__":
    t_start = time.time()
    page_to_jsonfile = PageToJsonFile(delay=0)
    run_thr_def(num_pages=100, count_thr=10, page_to_json=page_to_jsonfile)
    t_end = time.time()
    print(f"==> work_time_thr: {t_end - t_start}")
