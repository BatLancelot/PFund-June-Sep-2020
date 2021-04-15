n = int(input())
word = input()

string_list = []
filtered_list = []

for _ in range(n):
    sentence = input()
    string_list.append(sentence)
    if word in sentence:
        filtered_list.append(sentence)

print(f'{string_list}\n{filtered_list}')
