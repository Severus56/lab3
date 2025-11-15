alphabet_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
alphabet_upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
encrypted_text = input().strip()
first_decrypted_char = input().strip()
K = 0
if encrypted_text[0] in alphabet_lower and first_decrypted_char in alphabet_lower:
    idx_enc = alphabet_lower.index(encrypted_text[0])
    idx_dec = alphabet_lower.index(first_decrypted_char)
    K = (idx_enc - idx_dec) % 33
elif encrypted_text[0] in alphabet_upper and first_decrypted_char in alphabet_upper:
    idx_enc = alphabet_upper.index(encrypted_text[0])
    idx_dec = alphabet_upper.index(first_decrypted_char)
    K = (idx_enc - idx_dec) % 33
decrypted_text = []
for char in encrypted_text:
    if char in alphabet_lower:
        idx_enc = alphabet_lower.index(char)
        idx_dec = (idx_enc - K) % 33
        decrypted_text.append(alphabet_lower[idx_dec])
    elif char in alphabet_upper:
        idx_enc = alphabet_upper.index(char)
        idx_dec = (idx_enc - K) % 33
        decrypted_text.append(alphabet_upper[idx_dec])
    else:
        decrypted_text.append(char)
print(''.join(decrypted_text))