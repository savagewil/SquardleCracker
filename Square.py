from typing import Set

from DictIndex import DictIndex


class Square:
    def __init__(self, letter, starts, words):
        self.letter = letter
        self.starts = starts
        self.words = words
        self.neighbors: Set[Square] = set()

    def add_neighbor(self, neighbor):
        if neighbor is not None:
            self.neighbors.add(neighbor)

    def search(self, dictionary: DictIndex, seen: set):
        if dictionary is not None:
            seen.add(self)
            if dictionary.end:
                words = {""}
            else:
                words = set()

            for neighbor in self.neighbors:
                if (not neighbor in seen) and neighbor.words > 0:
                    words.update(neighbor.search(dictionary.prefix(neighbor.letter), seen))
            # print(words)
            seen.remove(self)
            return {self.letter + word for word in words}
        return {}

    @staticmethod
    def from_string(string):
        letter, starts, words = string.split("|")
        return Square(letter, int(starts), int(words))

