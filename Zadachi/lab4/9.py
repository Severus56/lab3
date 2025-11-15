N = int(input())
C1 = input().strip()
C2 = input().strip()

result = ''.join([C1 if i % 2 == 0 else C2 for i in range(N)])
print(result)