word = input()

capitals = []
capitals_2 = ''

# capitals.append([word[i].isupper() for i in range(len(word))])
# print(capitals)

for i in range(len(word)):  # loop trough the letter positions
    if word[i].isupper():  # Check if letter at position i is Uppercase
        capitals.append(i)  # Collect the letter positions to a list
        capitals_2 += ''.join(word[i])  # Add capitals to form a word


print(capitals)
print(capitals_2)
