from nq.filters import Filter


class recurse_until:
    pass


def _common_iterable(obj):
    if isinstance(obj, dict):
        return obj
    else:
        return (index for index, value in enumerate(obj))


def nested_query(iterable, *path_parts, **kwargs):
    results = []
    depth = kwargs["depth"] if "depth" in kwargs else 0
    flags = []
    if "flags" in kwargs:
        flags = kwargs["flags"]
        if not isinstance(flags, list):
            flags = [flags]

    if len(path_parts) > 0:
        path_part = path_parts[0]
        if isinstance(path_part, Filter):
            for key in _common_iterable(iterable):
                if path_part.check_filter(key, iterable[key], depth):
                    if len(path_parts) == 1:
                        results.append(iterable[key])
                    else:
                        results += nested_query(
                            iterable[key], *path_parts[1::], depth=depth + 1
                        )
        elif path_part is recurse_until:
            if len(path_parts) > 1:
                test_next_part = nested_query(
                    iterable, *path_parts[1::], depth=depth + 1
                )
                if not test_next_part and type(iterable) in (list, dict):
                    for key in _common_iterable(iterable):
                        if len(path_parts) == 1:
                            results.append(iterable[key])
                        else:
                            results += nested_query(
                                iterable[key], *path_parts, depth=depth + 1
                            )
                else:
                    results += test_next_part
        else:
            found_item = False
            try:
                iterable[path_part]
                found_item = True
            except Exception:
                pass
            if found_item:
                if len(path_parts) == 1:
                    results.append(iterable[path_part])
                elif type(iterable[path_part]) in (tuple, dict, list):
                    results += nested_query(
                        iterable[path_part], *path_parts[1::], depth=depth + 1
                    )
        if depth == 0 and len(results) == 1:
            return results[0]
        else:
            if Flags.FIRST_RESULT in flags:
                return results[0]
            elif Flags.LAST_RESULT in flags:
                return results[-1]
            else:
                return results
    else:
        return iterable


class Tree:
    def __init__(self, data):
        self.data = data

    def query(self, *path_parts, **kwargs):
        return nested_query(self.data, *path_parts, **kwargs)
