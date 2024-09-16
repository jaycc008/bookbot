def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_count = count_words(text)
    chars_dict = count_chars(text)
    dict_list = create_dict_list(chars_dict)
    dict_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in the document\n")

    for dict in dict_list:
        print(f"The '{dict['name']}' character was found {dict['num']} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars_dict = {}

    for char in text.lower():
        if char.isalpha():
            if char in chars_dict:
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1

    return(chars_dict)

def create_dict_list(dict):
    dict_list = []
    for key, value in dict.items():
        dict_list.append({"name": key, "num": value})

    return dict_list

def sort_on(dict):
    return dict["num"]

main()