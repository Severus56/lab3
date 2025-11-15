s = input().strip()
words = s.split()
if not words:
    print(0)
else:
    min_length = min(len(word) for word in words)
    print(min_length)