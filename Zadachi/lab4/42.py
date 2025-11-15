s = input().strip()
words = s.split()
count = 0
for word in words:
    if word and word[0] == word[-1]:
        count += 1

print(count)