"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
 
import csv



def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open(
        "data.csv",
        "r",
    ) as f:
        data = csv.reader(f, delimiter="\t")

        A = []
        for row in data:
            n = int(row[1])
            A.append(n)
        suma = sum(A)
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    with open(
        "data.csv",
        "r",
    ) as f:

        data = f.readlines()

        letters = [row[0] for row in data]
        c = []
        num = [letters.count(item) for item in ["A", "B", "C", "D", "E"]]
        z = ["A", "B", "C", "D", "E"]
        A = list(zip(z, num))

    return A


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open(
        "data.csv",
        "r",
    ) as f:
        data = csv.reader(f, delimiter="\t")

        letters = []
        numbers = []
        for row in data:
            letters.append(row[0])
            numbers.append(row[1])

        l = list(zip(letters, numbers))

    sum = {}

    for letter, number in l:
        if letter in sum:
            sum[letter] += int(number)
        else:
            sum[letter] = int(number)

    result = sorted([(letter, suma) for letter, suma in sum.items()])

    return result


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

    import csv

    with open(
        "data.csv",
        "r",
    ) as f:
        data = csv.reader(f, delimiter="\t")

        l = []
        for row in data:
            l.append(row[2])

    import re

    meses = []
    for fecha in l:
        match = re.search(r"\d{4}-(\d{2})-\d{2}", fecha)
        if match:
            mes = match.group(1)
            meses.append(mes)
        else:
            print(f"Error: Formato de fecha inválido - Fecha: {fecha}")

    from collections import Counter

    conteo = Counter(meses)
    conteo = list(conteo.items())
    conteo = sorted(conteo)
    return conteo


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    import csv

    with open(
        "data.csv",
        "r",
    ) as f:
        data = csv.reader(f, delimiter="\t")

        d = {}
        l = []
        for row in data:
            tupla = (row[0], row[1])
            l.append(tupla)
        r = []

        for letter, number in l:
            if letter in d:
                d[letter].append(number)
            else:
                d[letter] = [number]

        resultado = []

        for letter, number in d.items():
            maximo = int(max(number))
            minimo = int(min(number))
            resultado.append((letter, maximo, minimo))
            resultado = sorted(resultado)

    return resultado


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    import csv

    with open(
        "data.csv",
        "r",
    ) as f:
        data = csv.reader(f, delimiter="\t")

        d = {}
        for row in data:
            l = row[4]
            for item in l.split(","):
                key, value = item.split(":")
                value = int(value)
                if key in d:
                    d[key].append(value)
                else:
                    d[key] = [value]

    resultado = []
    for key, value in d.items():
        minimo = min(value)
        maximo = max(value)
        resultado.append((key, minimo, maximo))

    resultado = sorted(resultado)

    return resultado


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    import csv

    with open(
        "data.csv",
        "r",
    ) as f:
        data = csv.reader(f, delimiter="\t")

        lista = []
        for row in data:
            tupla = (row[1], row[0])
            lista.append(tupla)

    d = {}
    for number, letter in lista:
        if number in d:
            d[number].append(letter)
        else:
            d[number] = [letter]

    r = []

    for key, value in d.items():
        r.append((int(key), value))

    r = sorted(r)

    return r


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    import csv

    with open(
        "data.csv",
        "r",
    ) as f:
        data = csv.reader(f, delimiter="\t")

        lista = []
        for row in data:
            tupla = (row[1], row[0])
            lista.append(tupla)

    d = {}
    for number, letter in lista:
        if number in d:
            d[number].append(letter)
        else:
            d[number] = [letter]

    r = []

    for key, value in d.items():
        r.append((int(key), sorted(list(set(value)))))

    r = sorted(r)

    return r


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    import csv

    with open("data.csv", "r") as f:
        data = csv.reader(f, delimiter="\t")

        s = []
        for row in data:
            l = row[4]
            for item in l.split(","):
                key, _ = item.split(":")
                s.append(key)

    from collections import Counter

    s = Counter(s)
    s = dict(s)
    s = sorted(s.items())
    s = dict(s)

    return s


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

    import csv

    with open("data.csv", "r") as f:
        data = csv.reader(f, delimiter="\t")

        c4 = []
        c5 = []
        c1 = []
        for row in data:
            c1.append(row[0])
            c4.append(row[3])
            c5.append(row[4])

        c4 = [item.split(",") for item in c4]
        c5 = [item.split(",") for item in c5]

    cc4 = []
    cc5 = []
    for i in range(len(c4)):
        cc4.append(len(c4[i]))
        cc5.append(len(c5[i]))

    resultado = []

    for i in range(len(c1)):
        resultado.append((c1[i], cc4[i], cc5[i]))

    return resultado


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """

    import csv

    with open(
        "data.csv",
        "r",
    ) as f:
        data = csv.reader(f, delimiter="\t")

        s = []
        l0 = []

        for row in data:
            l0.append(row[1])
            s.append(row[3])

    s = [item.split(",") for item in s]

    d = {}

    lista = []

    for i in range(len(l0)):
        lista.append((l0[i], s[i]))

    for number, letters in lista:
        for item in letters:
            if item in d:
                d[item] += int(number)
            else:
                d[item] = int(number)

    d = sorted(d.items())
    d = dict(d)
    return d


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import csv

    with open(
        "data.csv",
        "r",
    ) as f:
        data = csv.reader(f, delimiter="\t")

        s = []
        l0 = []

        for row in data:
            l0.append(row[0])
            l = row[4]
            suma = 0
            for item in l.split(","):
                key, value = item.split(":")
                value = int(value)
                suma += value
            s.append(suma)

    lista = []
    for i in range(len(l0)):
        lista.append((l0[i], s[i]))

    sum = {}

    for letter, number in lista:
        if letter in sum:
            sum[letter] += int(number)
        else:
            sum[letter] = int(number)

    result = sorted([(letter, suma) for letter, suma in sum.items()])

    result = dict(result)

    return result
