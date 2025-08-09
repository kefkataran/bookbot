def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_num_words():
    text = get_book_text("books/frankenstein.txt")
    words = text.split()
    num_words = len(words)
    print(num_words)

def get_char_count():
    main_text = get_book_text("books/frankenstein.txt")
    text = main_text.lower()
    char_counts = {}

    #count characters
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    #convert dict to list of dicts
    characters = []
    for char, count in char_counts.items():
        characters.append({"char": char, "num": count})

    #sort by count, descending
    def sort_on(item):
        return item["num"]

    characters.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============",
    "Analyzing book found at books/frankenstein.txt...",
    "----------- Word Count ----------",
    "Found", get_num_words, "total words",
    "--------- Character Count -------",
    f"{entry['char']}: {entry['num']}",
    "============= END ===============")


get_char_count()