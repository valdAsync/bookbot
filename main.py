import collections


def count_words(text: str) -> int:
    return len(text.split())


def count_chars(text: str):
    return collections.Counter(text.lower())


def convert(dictionary):
    return [{key: value} for key, value in dictionary.items()]


def alpha_chars(dictionary):
    alpha_chars = {}
    for char, count in dictionary.items():
        if char.isalpha():
            alpha_chars[char] = count
    return alpha_chars


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    chars = count_chars(file_contents)
    alpha_characters = alpha_chars(chars)

    converted = convert(alpha_characters)
    sorted_converted = sorted(
        converted, key=lambda x: list(x.values())[0], reverse=True
    )

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"Number of words found: {count_words(file_contents)}")

    for char in sorted_converted:
        print(
            f"The letter {list(char.keys())[0]} appears {list(char.values())[0]} times"
        )

    print("--- End report ---")


if __name__ == "__main__":
    main()
