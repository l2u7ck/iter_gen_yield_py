class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):

        self.count = 0
        self.new_list = []

        for count in range(len(self.list_of_list)):
            for item in self.list_of_list[count]:
                if isinstance(item, list):
                    self.new_list += list(FlatIterator(item))
                else:
                    self.new_list += [item]

        return self

    def __next__(self):

        if len(self.new_list) - 1 < self.count:
            raise StopIteration

        item = self.new_list[self.count]
        self.count += 1

        return item


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
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
