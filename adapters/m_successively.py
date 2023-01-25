import time

from workers import PageToJsonFile


def run_suc(num_pages: int, page_to_jsonfile: PageToJsonFile) -> None:
    t_start = time.time()

    for page in range(1, num_pages + 1):
        page_to_jsonfile(page=page)

    t_end = time.time()
    print(f"==> work_time_suc: {t_end - t_start}")


if __name__ == "__main__":
    page_to_jsonfile = PageToJsonFile(delay=0)
    run_suc(num_pages=100, page_to_jsonfile=page_to_jsonfile)
