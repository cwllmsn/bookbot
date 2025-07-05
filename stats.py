def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return f"Found {num_words} total words"

def get_char_count(text):
    word_count = {}
    to_lower_case = text.lower()
    for char in to_lower_case:
        if char.isalpha():
            if char in word_count:
                word_count[char] += 1
            else:
                word_count[char] = 1
    return word_count

def sort_on(items):
    return items["count"]

def get_sort_on_value(dictionary):
    items = []
    for char, count in dictionary.items():
        items.append({"char": char, "count": count})
    sorted_items = sorted(items, key=sort_on, reverse=True)
    return sorted_items
