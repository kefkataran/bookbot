def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    characters = []
    for char, count in char_counts.items():
        characters.append({"char": char, "num": count})

    def sort_on(item):
        return item["num"]

    characters.sort(reverse=True, key=sort_on)
    return characters

# === Main Report Function ===
def create_report(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...\n")

    text = get_book_text(path)

    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words\n")

    print("--------- Character Count -------")
    characters = get_char_count(text)
    for entry in characters:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")