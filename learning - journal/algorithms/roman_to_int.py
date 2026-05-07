def roman_to_int(roman):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    digit = 0
    for i in range(len(roman) -1):
        if values[roman[i]] < values[roman[i+1]]:
            digit -= values[roman[i]]
        else:
            digit += values[roman[i]]
    digit += values[roman[-1]]
    return digit

print(roman_to_int("III"))      # 3
print(roman_to_int("IV"))       # 4
print(roman_to_int("IX"))       # 9
print(roman_to_int("LVIII"))    # 58
print(roman_to_int("MCMXCIV"))  # 1994