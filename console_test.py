import time

from adapters import m_multiprocessing, m_threading_amount_thr, m_threading, m_successively
from workers import PageToJsonFile


def run_test():

    num_pages = int(input("Enter number of pages: "))
    delay = float(input("Enter a delay between requests: "))
    page_to_jsonfile = PageToJsonFile(delay=delay)

    print(f"=> Working time without threading ↓")
    m_successively.run_suc(num_pages=num_pages, page_to_jsonfile=page_to_jsonfile)
    time.sleep(delay)

    print(f"=> Working time Threading no flow limit ↓")
    m_threading.run_thr(num_pages=num_pages, page_to_jsonfile=page_to_jsonfile)
    time.sleep(delay)

    amount_parallel: int = 10

    print(f"=> Working time Threading {amount_parallel} threads ↓")
    m_threading_amount_thr.run_thr(num_pages=num_pages, count_thr=amount_parallel, page_to_jsonfile=page_to_jsonfile)
    time.sleep(delay)

    print(f"=> Working time Multiprocessing {amount_parallel} processes ↓")
    m_multiprocessing.run(num_pages=num_pages, count_proc=amount_parallel, page_to_jsonfile=page_to_jsonfile)
    time.sleep(delay)


if __name__ == "__main__":
    run_test()
