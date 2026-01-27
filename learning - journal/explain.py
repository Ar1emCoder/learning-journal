# работа со сплит
file = "python - это круто"
parts = file.split('-') # разрежь по дефисам
print("split res = ", parts)

with open('PYTHON.txt', 'w') as f:
    f.write("Строка 1\n")
with open('PYTHON.txt', 'a') as f:
    f.write('Строка 2\n')
with open('PYTHON.txt', 'r') as f:
    print("Содержимое файла:", f.read())

try:
    with open('PYTHONn.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("Упс! такого файла нет")