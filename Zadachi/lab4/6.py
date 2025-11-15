C = input().strip()

if C in '0123456789':
    print("digit")
elif C in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
    print("lat")
else:
    print("rus")