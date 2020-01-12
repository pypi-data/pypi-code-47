from collections.abc import Iterable
from itertools import cycle
from multiprocessing.pool import Pool, ThreadPool
from time import sleep
from warnings import warn


def is_iter(obj):
    """
    Check if an object is an iterable.

    Args:
        obj: Object

    Returns:
        boolean
    """
    return isinstance(obj, Iterable) and not isinstance(obj, str)


def is_generator(iterable):
    """
    Check if an iterable is a generator.

    Args:
        iterable: Iterable.

    Returns:
        boolean
    """
    return hasattr(iterable, '__iter__') and not hasattr(iterable, '__len__')


# This is defined outside the loading function so it does not restart every time the function is called.
bars = cycle(r'-\|/')
dots = cycle(('   ', '.  ', '.. ', '...'))


def loading(kind='spinning bar'):
    """
    Prints loading string. Every time this function is called, the string changes.

    Args:
        kind: Kind of string. 'spinning bar' or 'dots'.

    Returns:
        string
    """
    if 'bar' in kind:
        global bars
        iterable = bars
    elif 'dot' in kind:
        global dots
        iterable = dots
    else:
        raise ValueError(
            f"Kind {kind} not supported. Please choose between 'bar' or 'dot'."
        )
    # get next from the global variable
    i = next(iterable)
    return i


def progress(ratio=0, width=30):
    """ Prints progress bar

    Parameters:
        ratio: Completed ratio.
        width: progress bar width.
    """
    # If the action is completed, will skip a line at the end.
    if ratio == 1:
        end = '\n'
    else:
        # Otherwise will continue to print in the same line.
        end = ''
    # Calculate the numbers of '#" in the left.
    left = int(width * ratio)
    # Calculate the number of spaces i the right.
    right = width - left
    # Print the bar, the percentage and a loading indicator.
    print(f'\r[{"#" * left}{" " * right}] {ratio * 100:.0f}% {loading()}',
          sep='',
          end=end,
          flush=True)


def lazy_pool(pool, function, args, disable_return=True):
    """
    Run pool lazily, suitable when the argument is a generator.

    This function is designed to work mostly with generators So by default it returns None. The reason for this is
    because generator are usually used for very long iterables, and storing all returns would exhaust memory.

    Args:
        pool: Pool instance.
        function: Function to be executed in the pool.
        args: Function arguments list.
        disable_return: Whether to store and return or not. When the argument is a generator, it exhaust memory.

    Returns:
        the return of the function, or None when disable_return=True
    """
    result = pool.imap_unordered(function, args)
    i = 0
    return_list = []
    while True:
        try:
            row = result.next()
        except StopIteration:
            break
        if not disable_return:
            return_list.append(row)
        i += 1
        print(f'\r{i} loaded.')

    return return_list


# noinspection PyProtectedMember
def async_pool(pool, function, args):
    """
    Run asynchronous pool.

    Args:
        pool: Pool instance
        function: Function to be executed in the pool.
        args: List of function arguments

    Returns:
        The returns from the function.
    """
    # Run asynchronous multiprocessing
    if is_iter(args[0]):
        result = pool.starmap_async(function, args)
    else:
        result = pool.map_async(function, args)
    # creates a loop that only ends when the multiprocessing is done.
    while not result.ready():
        # Check how much jobs are remaining.
        remaining = result._number_left * result._chunksize
        # Calculates the ratio
        ratio = (len(args) - remaining) / len(args)
        progress(ratio)
        sleep(.1)
    # close workers and get results.
    progress(1)
    pool.close()

    return result


def run(function, args, n_workers=None, thread=False, disable_return=False):
    """
    Run many instances of a function in parallel.

    Args:
        function: Function to be executed.
        args: Function arguments list.
        n_workers: Number of parallel workers to use. None to use all available.
        thread: True to use multi-threading, False to use multi-processing.
        disable_return: If args is a generator, should it disable or not the returns.

    Returns:
        Iterable with all returns from the function for each argument.
    """
    # Select the type o Pool
    if thread:
        pool = ThreadPool(n_workers)
    else:
        pool = Pool(n_workers)

    # If its a generator, then a lazy pool must be used.
    if is_generator(args):
        # Run pool.
        result = lazy_pool(pool, function, args, disable_return=disable_return)
        # If the user want the returns, get it and returns it.
        if not disable_return:
            # noinspection PyUnresolvedReferences
            return result.get()
    # But if not a generator, use asynchronous pool
    else:
        # Run pool.
        result = async_pool(pool, function, args)
        # If the use passed disable_returns=True, give a warning informing that parameter is only relevant when the
        # argument is  generator
        if disable_return:
            warn(
                'The argument disable_return is only relevant when args is a generator.'
            )
            return
        else:
            # get and return results
            return result.get()
