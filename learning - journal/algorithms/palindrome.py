def clean_string(s):
    chars = ''
    for i in s:
        if i.isalpha() or i.isdigit():
            chars += i
    return chars.lower()

def is_palindrome(s):
    cleaned = clean_string(s)
    return cleaned == cleaned[::-1]

print(is_palindrome("А роза упала на лапу Азора"))
print(is_palindrome("Hello"))
print(is_palindrome("12321"))