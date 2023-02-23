from adapters.request_json import PageToJsonFile
from workers import TestPool


def run_test() -> None:

    num_pages = int(input("\033[35m{}".format("Enter number of pages: ")))
    delay = float(input("Enter a delay between requests: "))
    amount_parallel = int(input("Enter the amount of parallelization: "))
    page_to_jsonfile = PageToJsonFile(delay=delay)

    test_requests = TestPool(
        num_pages=num_pages,
        page_to_jsonfile=page_to_jsonfile,
        delay=delay,
        amount_parallel=amount_parallel,
    )
    test_requests.result_successively()
    test_requests.result_threading_unlimited()
    test_requests.result_threading()
    test_requests.result_threading_semaphore()
    test_requests.result_multiprocessing()
    test_requests.result_multiprocessing_pool()


if __name__ == "__main__":
    run_test()
