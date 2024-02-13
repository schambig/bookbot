def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    only_letters_dict = get_only_letters_dict(num_chars)
    # print(text)
    # print(f'{num_words} words found in the document')
    # print(num_chars)
    # print(only_letters_dict)
    print(f'*** Begin report of {book_path} ***')
    print(f'{num_words} words found in the document')
    print()
    print(get_letters_report(only_letters_dict))
    print()
    print(f'*** End report ***')


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    # words = str(text).split()
    words = text.split()
    return len(words)


def get_num_chars(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def get_only_letters_dict(dict):
    only_letters = []
    for key, value in dict.items():
        if key.isalpha():
            only_letters.append({key: value})
    sorted_list = sorted(only_letters, key=lambda x: list(x.values())[0], reverse=True)
    return sorted_list


def get_letters_report(list):
    letters_report = ''
    for element in list:
        for key, value in element.items():
            letters_report += f"The '{key}' character was found {value} times.\n"
    return letters_report


main()

