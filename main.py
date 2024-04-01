def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    num_words = read_book(text)
    print(f"{num_words} found in the text")
    num_letters = count_letters(text)
    #print(num_letters)
    converted = []

    for letter in num_letters:
        new_dict = {"letter": letter, "numLetter": num_letters.get(letter)}
        converted.append(new_dict)

    converted.sort(reverse=True, key=sort_on)


    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()

    for d in converted:
        print(f"The '{d.get("letter")}' character was found {d.get("numLetter")} times")
    
def sort_on(dict):
    return dict["numLetter"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def read_book(text):
    words = text.split()
    return len(words)


def count_letters(text):
    text_norm = text.lower()
    counts = {}

    for letter in text_norm:
        position = ord(letter) - 97 #0-25
        condition = position < 0 or position > 25

        if condition:
            continue  

        if letter not in counts.keys():
            counts[letter] = 0
        
        counts[letter] = counts.get(letter) + 1

    return counts


main()