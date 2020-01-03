'''
get proxies
'''

from typing import List, Tuple

# import inspect
from loguru import logger

from simple_pp.jhao.ProxyGetter.getFreeProxy import GetFreeProxy
# from simple_pp.jhao.Util.utilFunction import verifyProxyFormat

SITE_LIST = [
    'freeProxy01',
    'freeProxy04',
    # 'freeProxy05',
    'freeProxy07',
    'freeProxy08',
    'freeProxy09',
    # 'freeProxy10', 'freeProxy11', 'freeProxy12',  # uncomment this for external proxies
    'freeProxy14',
    'freeProxy03'
]


def get_proxies(numb: int = 200) -> List[Tuple[str]]:
    ''' fetch numb proxies if possible

    attach source info

    freeProxy03:
    getattr(GetFreeProxy, SITE_LIST[-1])(count_no, start_page=1)

    fp03 = getattr(GetFreeProxy, SITE_LIST[-1])
    [*fp03()]  # default: end, start, 5, 1
    _ = [*fp03(1, 1)]  # 200

    ip_list = [*zip(_, [] * len(_))]

    '''

    if numb > 5000:
        logger.warning(
            f' {numb} is a rather big number, bad things may happen... We ll give it a shot though.'
        )

    ip_list = []

    # check out SITE_LIST[:-1]
    for source in SITE_LIST[:-1]:
        logger.debug(f' Trying {source}... ')
        func = getattr(GetFreeProxy, source)
        try:
            _ = [*func()]
        except Exception as exc:
            logger.debug(f'{source}: {exc}')
            _ = []

        ip_list.extend([*zip(_, [source] * len(_))])

        if len(ip_list) > numb - 1:
            # break
            return ip_list

    # try xici page by page if necessary
    source = SITE_LIST[-1]
    fail_flag = -1
    for page in range(1, 2985):
        func = getattr(GetFreeProxy, source)
        try:
            _ = [*func(page, page)]

        except Exception as exc:
            logger.debug(f'{source}: {exc}')
            _ = []

        if _:
            fail_flag = 0
        else:
            fail_flag += -1

        ip_list.extend([*zip(_, [source] * len(_))])

        if len(ip_list) > numb - 1:
            break

        if fail_flag < -4:
            logger.warning(
                '\n\t Too many consecutive failures, giveing up... ')
            break

    if len(ip_list) < numb:
        logger.warning(
            f'\n\t Got {len(ip_list)}, that\'s the best we can do right now')

    return ip_list
