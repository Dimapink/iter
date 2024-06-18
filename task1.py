class FlatIterator:

    def __init__(self, list_of_list):
        self.max_value = len(list_of_list)
        self.list_of_list = list_of_list
        self.flat = iter([element for innerList in self.list_of_list for element in innerList])

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.flat)


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item, f"{flat_iterator_item=}"

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None], \
        f"{list(FlatIterator(list_of_lists_1))=}"


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    a = FlatIterator(list_of_lists_1)
    print(list(a))
    # print(next(a))
    # print(next(a))
    # print(next(a))

if __name__ == '__main__':
    test_1()