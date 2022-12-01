from file_handler import load_file_content, filtrate_calories_data
import os


class Elf():
    def __init__(self, id: int, items=[]):
        self.id = id
        self.items = items
        self.calories = self.total_calories_carried()

    def __repr__(self) -> str:
        return repr((f'id: {self.id}', f'kcal: {self.calories}', f'items: {len(self.items)}'))

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

    def sort_elves_by_calories(self):
        self.elves = sorted(self.elves, key=lambda elf: elf.calories)


if __name__ == "__main__":

    project = ElfOnAShelf()

    fp = os.path.dirname(__file__)

    file_content = load_file_content(os.path.join(fp, 'calories'))
    filtrated_data = filtrate_calories_data(file_content)

    project.load_calories_data(filtrated_data)
    project.sort_elves_by_calories()

    print(project.elves[-1]) # part 1

    print(project.elves[-1:-4:-1])
    top3_tot = sum(elf.calories for elf in project.elves[-1:-4:-1])
    print(top3_tot) # part 2