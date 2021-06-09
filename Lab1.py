# Вариант 2. Плеханов Егор, гр. ПИ-18У

# ============== Задание № 1 ==============
def tryParseFloatValue(inputString):
    try:
        return float(inputString)
    except:
        return None


count = 10
result = 0
print("Введите последовательность из 10 вещественных чисел (через Enter): \n")
for i in range(0, count):
    inputValue = tryParseFloatValue(input())
    if (inputValue is not None and int(inputValue) % 5 == 0):
        result += 1
print(f"Кол-во чисел, обладающих целой частью кратной 5 равно {result}")

# ============== Задание № 2 ==============
def removeRepeatingSymbols(text):
    result = ""
    str = []
    lastSymbol = ""
    for word in text.split(' '):
        for symbol in word:
            if (symbol not in str or symbol != lastSymbol):
                str.append(symbol)
                lastSymbol = symbol
        result += "".join(str) + " "
        str = []
    return result


text = input("Введите текст: ")
print(f"\nТекст без повторений в словах: \n{removeRepeatingSymbols(text)}")