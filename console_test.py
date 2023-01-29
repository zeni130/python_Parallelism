import time

from adapters import (m_multiprocessing, m_successively, m_threading,
                      m_threading_amount_thr, m_threading_semaphore)
from workers import PageToJsonFile


def run_test():

    num_pages = int(input("Enter number of pages: "))
    delay = float(input("Enter a delay between requests: "))
    page_to_jsonfile = PageToJsonFile(delay=delay)

    print(f"=> Working time without threading ↓")
    t_start = time.time()
    m_successively.run_suc(num_pages=num_pages, page_to_jsonfile=page_to_jsonfile)
    t_end = time.time()
    print(f"==> work_time_suc: {t_end - t_start}")
    time.sleep(delay)

    print(f"=> Working time Threading no flow limit ↓")
    t_start = time.time()
    m_threading.run_thr(num_pages=num_pages, page_to_jsonfile=page_to_jsonfile)
    t_end = time.time()
    print(f"==> work_time_thr: {t_end - t_start}")
    time.sleep(delay)

    amount_parallel: int = 10

    print(f"=> Working time Threading, {amount_parallel} threads ↓")
    t_start = time.time()
    m_threading_amount_thr.run_thr(
        num_pages=num_pages,
        count_thr=amount_parallel,
        page_to_jsonfile=page_to_jsonfile,
    )
    t_end = time.time()
    print(f"==> work_time_thr: {t_end - t_start}")
    time.sleep(delay)

    print(f"=> Working time Threading with semaphore, {amount_parallel} threads ↓")
    t_start = time.time()
    m_threading_semaphore.run_thr(
        num_pages=num_pages,
        count_thr=amount_parallel,
        page_to_jsonfile=page_to_jsonfile,
    )
    t_end = time.time()
    print(f"==> work_time_thr: {t_end - t_start}")
    time.sleep(delay)

    print(f"=> Working time Multiprocessing, {amount_parallel} processes ↓")
    t_start = time.time()
    m_multiprocessing.run(
        num_pages=num_pages,
        count_proc=amount_parallel,
        page_to_jsonfile=page_to_jsonfile,
    )
    t_end = time.time()
    print(f"==> work_time_multiproc: {t_end - t_start}")
    time.sleep(delay)


if __name__ == "__main__":
    run_test()
