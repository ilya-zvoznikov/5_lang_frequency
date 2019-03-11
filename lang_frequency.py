import sys
from collections import Counter
import re


def load_data(filepath):
    words_list = []
    with open(filepath, 'r') as file_handler:
        for line in file_handler:
            words_list += [elem.lower() for elem in re.findall(r'\w+', line)]
    return words_list


def get_most_frequent_words(text):
    counter = Counter(text)
    return [elem[0] for elem in counter.most_common(10)]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        print('Не указан путь к файлу')
        exit()

    print('Десять самых популярных слов в тексте:')
    print(*get_most_frequent_words(load_data(filepath)), sep=', ')
