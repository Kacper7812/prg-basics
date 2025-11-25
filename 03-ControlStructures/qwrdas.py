plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    code = ord(char)      # kod znaku
    new_code = code + 1   # przesunięcie o 1
    new_char = chr(new_code)
    encrypted_text += new_char

print(f'Plain text: {plain_text}')
print(f'Encrypted:  {encrypted_text}')