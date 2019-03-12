import os
import re
import sys
from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as file_handler:
            text = file_handler.read()
        return text
    except UnicodeDecodeError:
        return None


def process_data(text):
    return [word for word in re.findall(r'\w+', text.lower())]


def get_most_frequent_words(words, number_of_words):
    counter = Counter(words)
    return [word for word, count in counter.most_common(number_of_words)]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        sys.exit('Не указан путь к файлу')

    text = load_data(filepath)

    if not text:
        exit('Файл не найден или данные не корректны')

    number_of_words = 10
    print('%s самых популярных слов в тексте:' % number_of_words)
    print(*get_most_frequent_words(process_data(text), number_of_words),
          sep=', ')
