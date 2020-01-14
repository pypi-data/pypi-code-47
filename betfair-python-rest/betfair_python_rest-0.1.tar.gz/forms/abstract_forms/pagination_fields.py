from dataclasses import dataclass


@dataclass
class RecordPagination:
    '''
    Abstract class for request which used pagination fields

    :param from_record: Specifies the first record that
    will be returned. Records start at index
    zero, not at index one.

    :param record_count: Specifies how many records will
    be returned from the index position 'fromRecord'.
    Note that there is a page size limit of 1000.
    A value of zero indicates that you would like
    all records (including and from 'fromRecord')
     up to the limit.
    '''
    from_record: int = None
    record_count: int = None

