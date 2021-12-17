import re
import docx2txt
from bloom import bloom_filter_analyzer
from linear import linear_search_analyzer


def main():
    document = docx2txt.process("doc.docx")
    string = re.sub(r'[^a-zа-яA-Za-zё-]', ' ', document)
    string = re.sub(r'[\s]+', ' ', document)
    data = string.split(" ")

    word = input('Введите слово для поиска: ')
    print(bloom_filter_analyzer(data, word))
    print(linear_search_analyzer(data, word))


main()
