"""
    Ahira Justice, ADEFOKUN
    justiceahira@gmail.com
"""


import os


def readFile(filename):
    assert os.path.exists(filename), 'Cannot find the file: %s' % (filename)
    file = open(filename, 'r')
    par = []
    content = []
    for line in file:
        newLine = line.split()
        if newLine == []:
            content.append(par)
            par = []
        else:
            for i in list(range(len(newLine))):
                newLine[i] = float(newLine[i])
                
            par.append(newLine)

    file.close()
    return content


def writeToFile(output, filename, mode):
    file = open(filename, mode)
    file.write(output)
    file.close()
