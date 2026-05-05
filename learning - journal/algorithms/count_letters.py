def count_letters(text):
    book_letters = {}
    for i in text:
        if i.isalpha():
            i = i.lower()
            if i not in book_letters:
                book_letters[i] = 1
            else:
                book_letters[i] += 1
    return book_letters

print(count_letters('А роза упала на лапу Азора'))