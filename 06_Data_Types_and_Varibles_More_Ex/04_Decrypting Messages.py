key = int(input())
num_of_lines = int(input())

message = []

for _ in range(num_of_lines):
    char = input()
    ascii_code = ord(char)
    decoded_char = ascii_code + key
    ascii_code = chr(decoded_char)
    message.append(ascii_code)

print(''.join(message))
