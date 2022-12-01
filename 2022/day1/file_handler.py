import os
from pprint import pprint

def load_file_content(filepath):
    with open(filepath) as f:
        lines = f.readlines()

    return lines

def filtrate_calories_data(file_content, debug=False):
    '''optimize - create classes in this loop'''
    elves = []

    _temp_elf = []
    for idx, line in enumerate(file_content):
        if line != "\n":
            _temp_elf.append(int(line.split('\n')[0]))
        else:
            elves.append(_temp_elf)
            _temp_elf = []

    if debug:
        pprint(elves)
        print(len(elves))

    return elves


if __name__ == "__main__":
    fp = os.path.dirname(__file__)

    file_content = load_file_content(os.path.join(fp, 'calories'))

    filtrated_data = filtrate_calories_data(file_content, debug=True)