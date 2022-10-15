
import re

with open("<ruta al archivo>/codigos_postales.txt", encoding="utf-8") as f_codigos_postales:
    codigos = {}
    for linea in f_codigos_postales:
        res1 = re.search(r"[\d ]+([^\d]+[a-z])\s(\d+)", linea)
        if res1:
            ciudad, cp = res1.groups()
            if ciudad in codigos:
                codigos[ciudad].add(cp)
            else:
                codigos[ciudad] = {cp}

with open("<ruta al archivo>/ciudades.txt", encoding="utf-8") as f_ciudades:
    for linea in f_ciudades:
        res2 = re.search(r"^[0-9]{1,2}\.\s+([\w\s-]+\w)\s+[0-9]", linea)
        ciudad = res2.group(1)
        print(ciudad, codigos[ciudad])
        print('\n')
