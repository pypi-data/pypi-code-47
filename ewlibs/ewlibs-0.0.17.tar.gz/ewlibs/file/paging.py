#mongodb数据分页
def file_paging(
        file_name,
        const_page_count="1000",
        const_skip_count="0",
        skip_head=True,
):
    def decorator(fn):
        def objectMethod(data_list, *args, **kwargs):
            with open(file_name, "r") as f:
                line = f.readline()
                if skip_head:
                    n = 0
                    dl = []
                else:
                    n = 1
                    dl = [
                        line,
                    ]
                while line:
                    line = f.readline()
                    n += 1
                    if n <= int(const_skip_count):
                        continue
                    dl.append(line)
                    if len(dl) == int(const_page_count):
                        fn(dl, *args, **kwargs)
                        print(f"finished:{n}")
                        dl = []
                if dl:
                    fn(dl, *args, **kwargs)
                    print(f"finished:{n}")

        return objectMethod

    return decorator
