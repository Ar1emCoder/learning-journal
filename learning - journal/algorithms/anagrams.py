def are_anagrams(word1, word2):
    if sorted(clean_string(word1)) == sorted(clean_string(word2)):
        print("Да, 2 слова состоят из одинаковых букв")
        return True
    else:
        print("Нет, 2 слова разные")
        return False

def clean_string(word):
    text1 = ''
    for i in word:
        if i.isalpha():
            text1 += i
    return text1.lower()

are_anagrams("Чурка", "ручка")
are_anagrams("Кот", "Ток")
are_anagrams("Listen", "Silent")
are_anagrams("Hello", "oleh")
are_anagrams("123", "321")
are_anagrams("", "")