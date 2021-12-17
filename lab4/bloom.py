import math
from bitarray import bitarray
from timeit import default_timer as timer


class BloomFilter(object):

    def __init__(self, false_possibility, number_expected_elements):
        self.ne_elements = number_expected_elements
        self.size = int(-1 * (self.ne_elements * math.log(false_possibility)) / (math.log(2) ** 2))
        self.n_hash = round((self.size / self.ne_elements) * math.log(2))

        self.bloom_filter = bitarray(self.size)
        self.bloom_filter.setall(0)

    def _hash_(self, item, index):
        simple_number = 31
        hash = 0
        for i in range(len(item)):
            hash = (simple_number * hash + index + ord(item[i])) % self.size
        return hash

    def add(self, item):
        for i in range(self.n_hash):
            self.bloom_filter[self._hash_(item, i)] = 1

    def notExist(self, item):
        for i in range(self.n_hash):
            if self.bloom_filter[self._hash_(item, i)] == 0:
                return True
        return False


def bloom_filter_analyzer(data, search_word):
    false_possibility = float(input("Введите вероятность ложного срабатывания: "))
    number_expected_elements = len(data)

    filter = BloomFilter(false_possibility=false_possibility, number_expected_elements=number_expected_elements)

    for element in set(data):
        filter.add(element)

    start = timer()
    if filter.notExist(search_word):
        result = f"Фильтр Блума: {search_word} не существует\n"
    else:
        result = f"Фильтр Блума: {search_word} возможно существует\n"
    end = timer()
    result += f"Потрачено: {(end - start):.6f} секунд\n\n"
    return result
