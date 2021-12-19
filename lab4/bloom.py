import copy
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
            hash += (simple_number * hash + index + ord(item[i]))
            hash %= self.size
        return hash

    def add(self, item):
        for i in range(self.n_hash):
            self.bloom_filter[self._hash_(item, i)] = 1

    def notExist(self, item):
        for i in range(self.n_hash):
            if self.bloom_filter[self._hash_(item, i)] == 0:
                return True
        return False


def bloom_filter_analyzer(data1, data2, search_word):
    false_possibility = float(input("Введите вероятность ложного срабатывания: "))

    number_expected_elements = len(data1)
    filter1 = BloomFilter(false_possibility=false_possibility, number_expected_elements=number_expected_elements)
    number_expected_elements = len(data1) + len(data2)
    filter2 = BloomFilter(false_possibility=false_possibility, number_expected_elements=number_expected_elements)

    for element in data1:
        filter1.add(element)
        filter2.add(element)

    for element in data2:
        filter2.add(element)

    ufilter = unite_filters(filter1, filter2)

    start = timer()
    if ufilter.notExist(search_word):
        result = f"Фильтр Блума: {search_word} не существует\n"
    else:
        result = f"Фильтр Блума: {search_word} возможно существует\n"
    end = timer()
    result += f"Потрачено: {(end - start):.6f} секунд\n\n"
    return result


def unite_filters(bloom1, bloom2):
    result = copy.deepcopy(bloom1)
    for i in range(len(result.bloom_filter)):
        if(bloom2.bloom_filter[i]) == 1:
            result.bloom_filter[i] = 1

    return result