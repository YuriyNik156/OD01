# Строка читается одинаково слева направо и справа налево - это палиндром. Например: "А роза упала на лапу Азора"

# 1. Очистить строчку: привести символы к нижнему регистру
# 2. Убрать все пробелы и знаки препинания
# 3. Проверить, читается ли строка одинаково слева направо и справа налево
# 4. Если строка читается одинаково - вернуть True, иначе - False

import re

def is_palindrome(s):
    s = s.lower()       # Привести символы к нижнему регистру
    s = re.sub(r'[^a-zа-я0-9]', '', s)      # Убрать пробелы и знаки препинания
    return s == s[::-1]     # Проверить, является ли строка палиндромом

print(is_palindrome("А роза упала на лапу Азора"))
print(is_palindrome("Кит на море романтик"))
print(is_palindrome("Ежу - хуже"))
print(is_palindrome("Эта строка не содержит палиндром"))
print(is_palindrome("No lemon - no melon"))
print(is_palindrome("Madam In Eden I'm Adam"))
print(is_palindrome("This is not palindrome"))
print(is_palindrome(""))

