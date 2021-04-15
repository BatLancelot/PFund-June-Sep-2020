text = input()

double_char = ''

for x in text:
    double_char += x + x  # OR: x * 2

print(double_char)

# with FOR Loop in 1 line:
# double_text = ''.join([x * 2 for x in text])
# print(double_text)

# With WHILE Loop:
# j = len(text)
# i = 0
# res = []
# while i < j:
#     res.append(text[i]*2)
#     i += 1
# result = "".join(res)
# print(result)
