__author__ = 'Dmitry'

def read(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()
        vCount, eCount = map(int, lines[0].split(" ", 1))
        array = map(tuple, (map(int, line.split(" ", 2)) for line in lines[1:]))
        return array, vCount, eCount