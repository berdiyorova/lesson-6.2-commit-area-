def roman_to_int(s):
    roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    num = 0
    i = len(s) - 1
    if i == 0:
        return roman[s[0]]

    while s != '':

        if i == 0 or roman[s[i]] <= roman[s[i - 1]]:
            num += roman[s[i]]
            s = s[:i]


        i = len(s) - 1
    return num
