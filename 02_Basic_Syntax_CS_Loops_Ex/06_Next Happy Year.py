import sys

year = int(input())
max_num = sys.maxsize


while year < max_num:
    year += 1
    ones = year % 10
    tens = (year % 100) // 10
    hundred = (year % 1000) // 100
    thousand = (year % 10000) // 1000

    if (ones == tens or ones == hundred or ones == thousand) or (tens == hundred or tens == thousand)\
            or hundred == thousand:
        continue

    print(year)
    break
