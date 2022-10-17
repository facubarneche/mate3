"""
2. Dado el siguiente código:
string = 'bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot'
result = re.findall('b[ao]t', string)
print(result)
Encuentra la expresión para que se emita: ['bat', 'bot']
"""

import re

def main():

    string = 'bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot'
    result = re.findall('b[ao]t', string)
    print(result)

if __name__ == '__main__':
    main()
