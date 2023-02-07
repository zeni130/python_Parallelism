from workers import PageToJsonFile, TestPool


def run_test() -> None:

    num_pages = int(input("Enter number of pages: "))
    delay = float(input("Enter a delay between requests: "))
    amount_parallel = int(input("Enter the amount of parallelization: "))
    page_to_jsonfile = PageToJsonFile(delay=delay)

    test = TestPool(
        num_pages=num_pages,
        page_to_jsonfile=page_to_jsonfile,
        delay=delay,
        amount_parallel=amount_parallel,
    )
    test.result_successively()
    test.result_threading_unlimited()
    test.result_threading()
    test.result_threading_semaphore()
    test.result_multiprocessing()
    test.result_multiprocessing_pool()


if __name__ == "__main__":
    run_test()
