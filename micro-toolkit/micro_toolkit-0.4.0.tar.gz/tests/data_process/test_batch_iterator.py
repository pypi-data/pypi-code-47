from micro_toolkit.data_process.batch_iterator import BatchingIterator


def test_batch_iterator():
    data = range(19)

    result = []

    bi = BatchingIterator(5)
    for i in bi(data):
        print(i)
        result.append(i)

    assert result == [
        [0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18]
    ]
