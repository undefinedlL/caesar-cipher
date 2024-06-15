import pyperclip
from caesar import SYMBOLS, MAX_KEY, encrypt, decrypt

while True:
    res = input("| Enter an action |\nEnter \'e\' to encrypt or \'d\' to decrypt message \n>>>  ").lower()
    
    if res == 'e':
        mode = 'encrypt'
        break
    elif res == 'd':
        mode = 'decrypt'
        break
    
while True:
    chars_qnt = MAX_KEY
    res = input(f'Enter the key (from 0 to {chars_qnt})\n>>>  ')
    if not res.isdecimal():
        continue
    
    if 0 <= int(res) <= chars_qnt:
        key = int(res)
        break
    
text = input('Enter a text: \n>>>  ')

if mode == 'encrypt':
    result = encrypt(text, key)
elif mode == 'decrypt':
    result = decrypt(text, key)
    

print(result, f'\n(This {mode}ed text copied to clipboard)')
pyperclip.copy(result)
        