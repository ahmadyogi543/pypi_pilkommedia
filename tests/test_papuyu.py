from statistika import papuyu


def average():
    columns = papuyu.get_header()[1:]

    for column in columns:
        print(papuyu.average(column))


def median():
    columns = papuyu.get_header()[1:]

    for column in columns:
        print(papuyu.median(column))


def modes():
    columns = papuyu.get_header()[1:]

    for column in columns:
        print(papuyu.modes(column))
