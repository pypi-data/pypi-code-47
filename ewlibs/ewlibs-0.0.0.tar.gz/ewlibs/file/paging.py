#mongodb数据分页
def file_paging(
        file_name,
        const_page_count="1000",
        const_skip_count="0",
):
    def decorator(fn):
        def objectMethod(data_list, *args, **kwargs):
            with open(file_name, "r") as f:
                line = f.readline().strip()
                dl = []
                n = 1
                while line:
                    if n <= int(const_skip_count):
                        dl = []
                        line = f.readline().strip()
                        n += 1
                        continue
                    dl.append(line)
                    n += 1
                    if len(dl) == int(const_page_count):
                        fn(dl, *args, **kwargs)
                        print(f"finished:{n}")
                        dl = []
                        line = f.readline().strip()
                    else:
                        line = f.readline().strip()
                if dl:
                    fn(dl, *args, **kwargs)
                    print(f"last finished:{n}")

        return objectMethod

    return decorator