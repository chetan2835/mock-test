s = input("Enter string (eg. swiss): ")

freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

result = -1
for ch in s:
    if freq[ch] == 1:
        result = ch
        break

print("first non repeating char. :", result)
