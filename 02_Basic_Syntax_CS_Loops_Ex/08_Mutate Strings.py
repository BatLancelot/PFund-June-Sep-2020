string_one = input()
string_two = input()

string_one = list(string_one)
string_two = list(string_two)

for i in range(len(string_one)):
    if string_two[i] not in string_one[i]:
        string_one[i] = string_two[i]
    else:
        continue
    new_string = ''.join(string_one)
    print(new_string)
