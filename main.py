import sys

def main() -> int:
    file = "books/frankenstein.txt"
    with open(file) as f:
        file_contents = f.read()
        print(f"--- Begin report of {file} ---")
        num_words = count_words(file_contents)
        print(f"{num_words} words found in the document\n")
        letters = count_letters(file_contents)
        letter_list = [(v, k) for k, v in letters.items()]
        letter_list.sort(reverse=True)

        for letter in letter_list:
            if letter[1].isalpha():
                print(f"The '{letter[1]}' character was found {letter[0]} times")

        print("--- End report ---")

    return 0
def count_words(text):
    return len(text.split())

def count_letters(text):
    letters = {}
    for letter in text:
        lowercase_char = letter.lower()
        if lowercase_char in letters:
            letters[lowercase_char] += 1
        else:
            letters[lowercase_char] = 1
    return letters

if __name__ == '__main__':
    sys.exit(main())
