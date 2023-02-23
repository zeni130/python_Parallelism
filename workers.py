import time

from adapters.m_multiprocessing import multiprocessing_def_run
from adapters.m_multiprocessing_pool import multiprocessing_pool_run
from adapters.m_successively import run_suc
from adapters.m_threading import run_thr
from adapters.m_threading_amount_thr import run_thr_def
from adapters.m_threading_semaphore import run_thr_sem


class TestPool:
    def __init__(self, num_pages, page_to_jsonfile, delay, amount_parallel):
        self.num_pages = num_pages
        self.page_to_jsonfile = page_to_jsonfile
        self.delay = delay
        self.amount_parallel = amount_parallel

    def result_successively(self) -> None:
        print("\033[34m{}".format("\n=> Working time successively ↓"))
        print("Num page ==> ", end="")
        t_start = time.time()
        run_suc(num_pages=self.num_pages, page_to_json=self.page_to_jsonfile)
        t_end = time.time()
        print("\033[34m{}".format(f"\n===> work_time_suc: {t_end - t_start}"))
        time.sleep(self.delay)

    def result_threading_unlimited(self) -> None:
        print("\033[34m{}".format(f"\n=> Working time Threading, {self.num_pages} threads ↓"))
        print("Num page ==> ", end="")
        t_start = time.time()
        run_thr(num_pages=self.num_pages, page_to_json=self.page_to_jsonfile)
        t_end = time.time()
        print("\033[34m{}".format(f"\n===> work_time_thr: {t_end - t_start}"))
        time.sleep(self.delay)

    def result_threading(self) -> None:
        print(
            "\033[34m{}".format(
                f"\n=> Working time Threading, {self.amount_parallel} threads ↓"
            )
        )
        print("Num page ==> ", end="")
        t_start = time.time()
        run_thr_def(
            num_pages=self.num_pages,
            count_thr=self.amount_parallel,
            page_to_json=self.page_to_jsonfile,
        )
        t_end = time.time()
        print("\033[34m{}".format(f"\n===> work_time_thr: {t_end - t_start}"))
        time.sleep(self.delay)

    def result_threading_semaphore(self) -> None:
        print(
            "\033[34m{}".format(
                f"\n=> Working time Threading with semaphore, {self.amount_parallel} threads ↓"
            )
        )
        print("Num page ==> ", end="")
        t_start = time.time()
        run_thr_sem(
            num_pages=self.num_pages,
            count_thr=self.amount_parallel,
            page_to_json=self.page_to_jsonfile,
        )
        t_end = time.time()
        print("\033[34m{}".format(f"\n===> work_time_thr_semaphore: {t_end - t_start}"))
        time.sleep(self.delay)

    def result_multiprocessing(self) -> None:
        print(
            "\033[34m{}".format(
                f"\n=> Working time Multiprocessing, {self.num_pages} processes ↓"
            )
        )
        print("Num page ==> ", end="")
        t_start = time.time()
        multiprocessing_def_run(
            num_pages=self.num_pages,
            count_proc=self.amount_parallel,
            page_to_json=self.page_to_jsonfile,
        )
        t_end = time.time()
        print("\033[34m{}".format(f"\n===> work_time_multiproc: {t_end - t_start}"))
        time.sleep(self.delay)

    def result_multiprocessing_pool(self) -> None:
        print(
            "\033[34m{}".format(
                f"\n=> Working time Multiprocessing pool, {self.amount_parallel} processes ↓"
            )
        )
        print("Num page ==> ", end="")
        t_start = time.time()
        multiprocessing_pool_run(
            num_pages=self.num_pages,
            count_proc=self.amount_parallel,
            page_to_json=self.page_to_jsonfile,
        )
        t_end = time.time()
        print("\033[34m{}".format(f"\n===> work_time_multiproc_pool: {t_end - t_start}"))
        time.sleep(self.delay)
