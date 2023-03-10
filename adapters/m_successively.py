import time

from adapters.request_json import PageToJsonFile


def run_suc(num_pages: int, page_to_json: PageToJsonFile) -> None:

    for page in range(1, num_pages + 1):
        page_to_json(page=page)


if __name__ == "__main__":
    t_start = time.time()
    page_to_jsonfile = PageToJsonFile(delay=0)
    run_suc(num_pages=100, page_to_json=page_to_jsonfile)
    t_end = time.time()
    print(f"==> work_time_suc: {t_end - t_start}")
