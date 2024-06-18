class FlatIterator:

    def __init__(self, list_of_list):
        self.max_value = len(list_of_list)
        self.list_of_list = list_of_list
        self.flat = []
        self.flatter(self.list_of_list)
        self.iter = iter(self.flat)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iter)

    def flatter(self, a):
        for element in a:
            if type(element) is list:
                self.flatter(element)
            else:
                self.flat.append(element)


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item, f"{flat_iterator_item}"

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!'], \
        f"{list(FlatIterator(list_of_lists_2))}"


if __name__ == '__main__':
    test_3()