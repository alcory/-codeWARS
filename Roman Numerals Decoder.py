

def solution(roman):
    roman_Dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_number = roman
    temporary_result = 0
    if 'IV' in roman:
        temporary_result = temporary_result + 4
        roman_number = roman_number.replace('IV','')
    if 'IX' in roman:
        temporary_result = temporary_result + 9
        roman_number = roman_number.replace('IX','')
    if 'XL' in roman:
        temporary_result = temporary_result + 40
        roman_number = roman_number.replace('XL','')
    if 'XC' in roman:
        temporary_result = temporary_result + 90
        roman_number = roman_number.replace('XC','')
    if 'CD' in roman:
        temporary_result = temporary_result + 400
        roman_number = roman_number.replace('CD','')
    if 'CM' in roman:
        temporary_result = temporary_result + 900
        roman_number = roman_number.replace('CM','')
    for rDigit in roman_number:
        temporary_result = temporary_result + roman_Dict.get(rDigit)
    return temporary_result

roman = 'CMXCIX'
print(solution(roman))

