import string
SYMBOLS = {    
    "lower_letters": string.ascii_lowercase,
    "upper_letters": string.ascii_uppercase,
    "special_symbols": string.punctuation,
    "digits": string.digits,
}

MAX_KEY = len(SYMBOLS['lower_letters'])

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
    if char in SYMBOLS['upper_letters']:
        res += shift(char, SYMBOLS['upper_letters'], key)
    elif char in SYMBOLS['lower_letters']:
        res += shift(char, SYMBOLS['lower_letters'], key)
    elif char in SYMBOLS['special_symbols']:
        res += shift(char, SYMBOLS['special_symbols'], key)
    elif char in SYMBOLS['digits']:
        res += shift(char, SYMBOLS['digits'], key)
    else:
        res += char
        
    return encrypt(text[1:], key, res)


def decrypt(text, key, res=''):
    if len(text) == 0: return res
    
    char = text[0]
    if char in SYMBOLS['upper_letters']:
        res += unshift(char, SYMBOLS['upper_letters'], key)
    elif char in SYMBOLS['lower_letters']:
        res += unshift(char, SYMBOLS['lower_letters'], key)
    elif char in SYMBOLS['special_symbols']:
        res += unshift(char, SYMBOLS['special_symbols'], key)
    elif char in SYMBOLS['digits']:
        res += unshift(char, SYMBOLS['digits'], key)
    else:
        res += char
        
    return decrypt(text[1:], key, res)
