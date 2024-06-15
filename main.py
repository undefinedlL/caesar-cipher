import pyperclip
import string

LOWER_LETTERS = string.ascii_lowercase
UPPER_LETTERS = string.ascii_uppercase
SPECIAL_SYMBOLS = string.punctuation
DIGITS = string.digits

def shift(sym, symbols, key):
    cur_index = symbols.find(sym)
    en_index = cur_index + key
    if en_index < len(symbols):
        return symbols[en_index ]
    else:
        return symbols[en_index % len(symbols)]

def unshift(sym, symbols, key):
    en_index = symbols.find(sym)
    de_index = en_index - key
    if de_index >= 0:
        return symbols[de_index]
    else: 
        return symbols[de_index % len(symbols)]
  
    
def encrypt(text, key, res=''):
    if len(text) == 0: return res
    
    char = text[0]
    if char in UPPER_LETTERS:
        res += shift(char, UPPER_LETTERS, key)
    elif char in LOWER_LETTERS:
        res += shift(char, LOWER_LETTERS, key)
    elif char in SPECIAL_SYMBOLS:
        res += shift(char, SPECIAL_SYMBOLS, key)
    elif char in DIGITS:
        res += shift(char, DIGITS, key)
    else:
        res += char
        
    return encrypt(text[1:], key, res)


def decrypt(text, key, res=''):
    if len(text) == 0: return res
    
    char = text[0]
    if char in UPPER_LETTERS:
        res += unshift(char, UPPER_LETTERS, key)
    elif char in LOWER_LETTERS:
        res += unshift(char, LOWER_LETTERS, key)
    elif char in SPECIAL_SYMBOLS:
        res += unshift(char, SPECIAL_SYMBOLS, key)
    elif char in DIGITS:
        res += unshift(char, DIGITS, key)
    else:
        res += char
        
    return decrypt(text[1:], key, res)


while True:
    res = input("| Enter an action |\nEnter \'e\' to encrypt or \'d\' to decrypt message \n>>>  ").lower()
    
    if res == 'e':
        mode = 'encrypt'
        break
    elif res == 'd':
        mode = 'decrypt'
        break
    
while True:
    chars_qnt = len(LOWER_LETTERS)
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
        