#Autofill README file with first comments from scripts in the directory

from os import listdir

readme = 'README.md'
content = listdir()

def get_list_py_files(list):
    result = set()
    for item in list:
        if '.py' in item:
            result.add(item)
    return result

def pure_py_files(files, target):
    f = open(target, 'r')
    files_in_target = set()
    result = set()
    for line in f.readlines():
        if not line.startswith('#'):
            files_in_target.add(line.split()[0])
    for item in files:
        if not item in files_in_target:
            result.add(item)
    f.close()
    return result

def get_descriptions(files):
    result = {}
    for item in files:
        f = open(item, 'r')
        desc = f.readline()
        if desc.startswith('#'):
            i = 0
            while desc[i + 1] == '#':
                i += 1
            desc = desc[i + 1:]
        else:
            desc = 'This file without description\n'
        f.close()
        result[item] = desc
    return result

def put_descriptions(descriptions, target):
    f = open(target, 'a')
    for k, v in descriptions.items():
        f.write('%s - %s' % (k, v))
        f.write('____\n')
    f.close()

put_descriptions(get_descriptions(pure_py_files(get_list_py_files(content), readme)), readme)
