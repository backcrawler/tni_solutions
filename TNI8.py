import requests
from bs4 import BeautifulSoup
from collections import namedtuple

parsingResult = namedtuple('Result', ['num_symbols', 'num_letters', 'num_words'])


def get_texts(url: str) -> bytes:
    r = requests.get(url)
    return r.content


def parse_html(raw_data: bytes) -> str:
    soup = BeautifulSoup(raw_data, 'lxml')
    res = soup.select("div:nth-of-type(2)")
    return res


def word_parser(word: str) -> tuple:
    counter = 0
    for char in word:
        if char.isalpha():
            counter += 1
    if counter != 0:
        flag = True
    else:
        flag = False
    return flag, counter


def parse_content(content: str) -> tuple:
    stripped = content.replace('\n', ' ').replace('\r', ' ')
    num_symbols = len(stripped)
    words = []
    words_raw = stripped.split()
    num_letters = 0
    for word in words_raw:
        res = word_parser(word)
        if res[0]:
            words.append(word)
        num_letters += res[1]
    num_words = len(words)
    return parsingResult(num_symbols, num_letters, num_words)


def main() -> None:
    with open('for_8.txt', 'r') as f:
        content = f.read()
    result = parse_content(content)
    print(result)


if __name__ == '__main__':
    main()
