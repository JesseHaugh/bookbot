word_count = {}
letter_filter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
with open("books/frankenstein.txt", "r") as f:
    file_contents = f.read()
    file_words = file_contents.split()
    print("--- Begin Report of books/frankenstine.txt ---")
    print(f"{len(file_words)} words found in the document\n")
    for char in file_contents:
        char = char.lower()
        if char in word_count:
            word_count[char] += 1
        else:
            word_count[char] = 1
    for word in letter_filter:
        print(f"The '{word}' charater was found {word_count[word]}")
    print('--- End Report ---')
