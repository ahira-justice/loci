import os


def read(filename):
    assert os.path.exists(filename), 'Cannot find the file: %s' % filename

    with open(filename, 'r') as _file:
        par = []
        content = []
        for line in _file:
            new_line = line.split()
            if not new_line:
                content.append(par)
                par = []
            else:
                for i in list(range(len(new_line))):
                    new_line[i] = float(new_line[i])

                par.append(new_line)

        return content


def write(output, filename, mode):
    assert mode in ['a', 'w'], 'Invalid write mode: %s' % mode

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, mode) as _file:
        _file.write(output)
