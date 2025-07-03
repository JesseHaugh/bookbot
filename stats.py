word_count = {}
letter_filter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def get_num_words(book_string):
    file_words = book_string.split()
    return len(file_words)

def letter_to_dict(book):
    letter_dict = {}
    for char in book:
        char = char.lower()
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1
    return dict_to_list(letter_dict)

def dict_to_list(dict):
    sort_list = []
    for letter in dict:
        sort_list.append({"char":letter, "num": dict[letter]})
    sort_list.sort(reverse=True, key=lambda d: d["num"])
    return sort_list



def get_num_words2(book_string,book_path):
        file_words = book_string.split()
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {len(file_words)} total words")
        for char in book_string:
            char = char.lower()
            if char in word_count:
                word_count[char] += 1
            else:
                word_count[char] = 1
        for word in letter_filter:
            print(f"{word}: {word_count[word]}")
        print('============= END ===============')


