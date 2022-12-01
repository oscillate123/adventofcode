from file_handler import load_file_content, filtrate_calories_data
import os


class Elf():
    def __init__(self, id: int, items=[]):
        self.id = id
        self.items = items
        self.calories = self.total_calories_carried()

    def total_calories_carried(self):
        _total = 0
        for item in self.items:
            _total += item
        return _total


class ElfOnAShelf:
    def __init__(self, elves=[], items=[]):
        self.elves = elves
        self.items = items
        self.biggus_elfus = ""

    def load_calories_data(self, data):
        for index, items in enumerate(data):
            _temp_elf = Elf(id=index, items=items)
            self.elves.append(_temp_elf)

    def find_elf_with_most_calories(self):
        strongest_elf = Elf(id=99999999)

        for elf in self.elves:
            if elf.calories > strongest_elf.calories:
                strongest_elf = elf

        self.biggus_elfus = strongest_elf


if __name__ == "__main__":

    project = ElfOnAShelf()

    fp = os.path.dirname(__file__)

    file_content = load_file_content(os.path.join(fp, 'calories'))
    filtrated_data = filtrate_calories_data(file_content)

    project.load_calories_data(filtrated_data)

    project.find_elf_with_most_calories()

    print(project.biggus_elfus.id)
    print(project.biggus_elfus.calories)