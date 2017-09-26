#user input required 
def roman_number(n):
    if (n == 1): return "I"
    if (n == 4): return "IV"
    if (n == 5): return "V"
    if (n == 9):  return "IX"
    if (n == 10): return "X"
    if (n == 40): return "XL"
    if (n == 50): return "L"
    if (n == 90): return "XC"
    if (n == 100): return "C"
    if (n == 400): return "CD"
    if (n == 500): return "D"
    if (n == 900): return "CM"
    if (n > 999): return "Number is out of range"

    for i in [1000, 100, 10, 1]:
        for j in [9 * i, 5 * i, 4 * i, i]:
            if (n >= j):
                return roman_number(j) + roman_number(n - j)
