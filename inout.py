"""
    Ahira Justice, ADEFOKUN
    justiceahira@gmail.com
"""


import os
import sys


def readFile(filename):
    assert os.path.exists(filename), 'Cannot find the file: %s' % (filename)
    file = open(filename, 'r')
    content = []
    for line in file:
        newLine = line.split()
        content.append(newLine)
    file.close()
    return content


def writeToFile(output, filename):
    file = open(filename, 'w')
    file.write(output)
    file.close()
    sys.exit()


def writeToString(output, out_print):
    for item in output:
        item = str(item)
        out_print += item + '\t'
    out_print += '\n'

    return out_print
