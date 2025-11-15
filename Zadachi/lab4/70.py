s = input()
open_index = s.find('(')
close_index = s.find(')')
if open_index != -1 and close_index != -1 and open_index < close_index:
    result = s[open_index + 1:close_index]
    print(result)
else:
    print("")
    print("123")
    print("123")
    print("123")
    print("123")
    print("123")