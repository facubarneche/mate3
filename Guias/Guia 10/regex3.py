"""
3. Dado el siguiente texto:
"Maria tiene 5 años, y su hermana Valeria tiene 2.
Rita y Pedro, sus primos, tienen 3."
Encuentra la expresión regular que extraiga y emita sólo los nombres.
"""

import re

def main():

    def regex(reg, txt):
        print(re.findall(reg, txt))

    reg = '[A-Z][a-z]*'
    txt = "Maria tiene 5 años, y su hermana Valeria tiene 2.\nRita y Pedro, sus primos, tienen 3."

    regex(reg, txt)


if __name__ == '__main__':
    main()
