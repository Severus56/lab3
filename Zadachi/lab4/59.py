full_path = input()
parts = full_path.split('.')
extension = parts[-1] if len(parts) > 1 else ''
print(extension)