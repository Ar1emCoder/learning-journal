def is_balanced(text):
    result = []
    total = {')': '(', ']': '[', '}': '{'} # словарь соответствия
    for i in text:
        if i in '([{':
            result.append(i)
        elif i in ')]}':
            if not result:
                return False
            top = result.pop()
            if total[i] != top:
                return False
    return not result

print(is_balanced("()"))        # True
print(is_balanced("([)]"))      # False
print(is_balanced("{[()]}"))    # True
print(is_balanced("("))         # False
print(is_balanced(""))          # True
