def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_char(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    chars_dict.sort(key=chars_dict.values())
    for char in chars_dict:
        print(f"The{char} character was found 46043 times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_char(text):
    count_dict = {}
    for ch in text:
        ch = ch.lower()
        count_dict[ch] = count_dict.get(ch, 0) + 1
    return count_dict

main()