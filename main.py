def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    all_character_count = count_chars(text)
    sorted_dict = all_char_dict_sorted_list(all_character_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for item in sorted_dict:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def count_chars(text):
    characters = {}
    for letter in text:
        lowered = letter.lower()
        if letter not in characters:
            characters [lowered] = 1
        elif letter in characters:
            characters [lowered] += 1
    return characters

def sort_on(d):
    return d["num"]

def all_char_dict_sorted_list(dict_to_sort):
    sorted_list = []
    for ch in dict_to_sort:
        sorted_list.append({"char": ch, "num": dict_to_sort[ch]})
    sorted_list.sort(reverse = True, key = sort_on)
    return sorted_list

main()
