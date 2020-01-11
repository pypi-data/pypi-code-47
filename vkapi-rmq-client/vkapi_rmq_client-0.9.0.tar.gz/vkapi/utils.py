from collections.abc import Iterable


def stringify_values(data):
    """Coerce iterable values to 'val1,val2,valN'

    Example:
        fields=['nickname', 'city', 'can_see_all_posts']
        --> fields='nickname,city,can_see_all_posts'

    :param data: dict
    :return: converted values dict
    """
    if not isinstance(data, dict):
        raise ValueError('Data must be dict. %r is passed' % data)

    values_dict = {}
    for key, value in data.items():
        items = []
        if isinstance(value, str):
            items.append(value)
        elif isinstance(value, Iterable):
            for v in value:
                item = str(v)
                items.append(item)
            value = ','.join(items)
        values_dict[key] = value
    return values_dict
